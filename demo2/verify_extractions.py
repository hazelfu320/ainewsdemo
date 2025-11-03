#!/usr/bin/env python3
"""
Verify message extractions by showing supporting excerpts from articles.

This script reads the extraction results and shows the actual text excerpts
that support each detected message, allowing for manual verification.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

import pandas as pd


def normalize_text(text: str) -> str:
    """Normalize text for processing."""
    if pd.isna(text):
        return ""
    return str(text).lower()


def find_meeting_excerpts(text: str) -> List[str]:
    """Find excerpts that support meeting occurrence detection."""
    excerpts = []
    
    # Patterns indicating meeting occurred
    patterns = [
        (r'\b(trump|donald trump|president trump)(.{0,50}?)(met|meeting|met with|met up|gathered|sat down|held.{0,20}meeting|had.{0,20}meeting)', 'name-first'),
        (r'\b(xi|xi jinping|president xi)(.{0,50}?)(met|meeting|met with|met up|gathered|sat down|held.{0,20}meeting|had.{0,20}meeting)', 'name-first'),
        (r'\b(trump.{0,30}?xi|xi.{0,30}?trump)(.{0,20}?)(meeting|summit|talks|encounter)', 'combined'),
        (r'\b(trump-xi|xi-trump)(.{0,20}?)(meeting|summit)', 'hyphenated'),
    ]
    
    for pattern, pattern_type in patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            # Extract context: 100 chars before and after
            start = max(0, match.start() - 100)
            end = min(len(text), match.end() + 100)
            excerpt = text[start:end].strip()
            # Clean up excerpt
            excerpt = '...' + excerpt if start > 0 else excerpt
            excerpt = excerpt + '...' if end < len(text) else excerpt
            excerpts.append(excerpt)
    
    return list(set(excerpts))  # Remove duplicates


def find_issue_excerpts(text: str, issue_name: str) -> List[str]:
    """Find excerpts that support a specific issue being discussed."""
    text_lower = normalize_text(text)
    excerpts = []
    
    # Issue keywords
    issue_keywords = {
        'trade': ['trade', 'tariff', 'tariffs', 'commerce', 'import', 'export', 'trade war', 'trade dispute'],
        'north korea': ['north korea', 'nkorea', 'nk', 'kim jong', 'nuclear', 'denuclearization'],
        'taiwan': ['taiwan'],
        'hong kong': ['hong kong', 'hk'],
        'south china sea': ['south china sea', 'scs'],
        'technology': ['technology', 'tech', '5g', 'huawei', 'semiconductor'],
        'currency': ['currency', 'yuan', 'rmb', 'exchange rate'],
        'ip rights': ['intellectual property', 'ip rights', 'patent', 'copyright'],
    }
    
    keywords = issue_keywords.get(issue_name, [])
    
    # Discussion patterns
    discussion_patterns = [
        r'\b(discussed|talked about|talked|spoke about|addressed|covered|focused on|centered on|revolved around|dealt with)',
    ]
    
    # Split into sentences for better context
    sentences = re.split(r'[.!?]+\s+', text)
    
    for sentence in sentences:
        sentence_lower = sentence.lower()
        # Check if sentence has both discussion verb and issue keyword
        has_discussion = any(re.search(pattern, sentence_lower, re.IGNORECASE) for pattern in discussion_patterns)
        has_issue = any(re.search(r'\b' + re.escape(kw) + r'\b', sentence_lower, re.IGNORECASE) for kw in keywords)
        
        if has_discussion and has_issue:
            # Also check if mentions Trump/Xi in proximity
            if re.search(r'\b(trump|xi|president)', sentence_lower, re.IGNORECASE):
                excerpts.append(sentence.strip())
        elif has_issue:
            # Issue keyword found, check nearby sentences
            # Include if sentence mentions Trump/Xi
            if re.search(r'\b(trump|xi|president)', sentence_lower, re.IGNORECASE):
                excerpts.append(sentence.strip())
    
    return excerpts[:5]  # Limit to 5 most relevant excerpts


def find_questions_excerpts(text: str) -> List[str]:
    """Find excerpts that support questions being answered."""
    excerpts = []
    
    patterns = [
        r'\b(answered|responded|replied)(.{0,30}?)(question|questions|query|queries)',
        r'\b(question|questions)(.{0,30}?)(answered|responded|addressed|addressing)',
        r'\b(q&a|q and a|question.{0,20}answer)',
        r'\b(asked|asking)(.{0,30}?)(trump|xi|president)(.{0,50}?)(answered|responded|said|replied)',
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            # Extract sentence containing the match
            sentence_start = text.rfind('.', 0, match.start()) + 1
            sentence_end = text.find('.', match.end())
            if sentence_end == -1:
                sentence_end = len(text)
            
            excerpt = text[sentence_start:sentence_end].strip()
            excerpts.append(excerpt)
    
    return list(set(excerpts))


def find_commentary_excerpts(text: str) -> List[str]:
    """Find excerpts that support external commentary detection."""
    excerpts = []
    
    # Commentary patterns
    commentary_patterns = [
        r'\b(said|stated|commented|remarked|noted|observed|suggested|indicated|expressed|claimed|added)',
    ]
    
    # Commentator indicators
    commentator_indicators = [
        r'\b(analyst|expert|official|spokesperson|spokesman|spokeswoman|minister|secretary|ambassador)',
        r'\b(white house|state department|chinese.{0,20}foreign.{0,20}ministry)',
    ]
    
    # Split into sentences
    sentences = re.split(r'[.!?]+\s+', text)
    
    for sentence in sentences:
        sentence_lower = sentence.lower()
        has_commentary = any(re.search(pattern, sentence_lower, re.IGNORECASE) for pattern in commentary_patterns)
        has_commentator = any(re.search(pattern, sentence_lower, re.IGNORECASE) for pattern in commentator_indicators)
        
        if has_commentary and has_commentator:
            # Check if sentence mentions Trump/Xi or meeting
            if re.search(r'\b(trump|xi|meeting|summit|talks)', sentence_lower, re.IGNORECASE):
                excerpts.append(sentence.strip())
    
    return excerpts[:5]  # Limit to 5 excerpts


def format_excerpts(excerpts: List[str], max_length: int = 200) -> str:
    """Format excerpts for display, truncating if too long."""
    if not excerpts:
        return "  No supporting excerpts found"
    
    formatted = []
    for i, excerpt in enumerate(excerpts, 1):
        if len(excerpt) > max_length:
            excerpt = excerpt[:max_length] + "..."
        formatted.append(f"  [{i}] {excerpt}")
    
    return "\n".join(formatted)


def main():
    data_file = Path(__file__).parent.parent / 'data' / 'trump_xi_meeting_fulltext_dedup-1657.csv'
    results_file = Path(__file__).parent / 'message_extraction_results.csv'
    
    if not data_file.exists():
        print(f"Error: Data file not found: {data_file}", file=sys.stderr)
        sys.exit(1)
    
    if not results_file.exists():
        print(f"Error: Results file not found: {results_file}", file=sys.stderr)
        print("Please run extract_key_messages.py first.", file=sys.stderr)
        sys.exit(1)
    
    # Load data
    print("Loading article data and extraction results...")
    df_articles = pd.read_csv(data_file)
    df_results = pd.read_csv(results_file)
    
    print(f"Found {len(df_results)} articles with extraction results\n")
    print("="*80)
    print("VERIFICATION: Supporting Excerpts for Detected Messages")
    print("="*80)
    
    # Process each article
    for idx, result in df_results.iterrows():
        article_idx = int(result['index'])
        title = result['title']
        source = result['source']
        body = df_articles.iloc[article_idx]['body']
        
        if pd.isna(body):
            body = ""
        
        print(f"\n{'='*80}")
        print(f"Article {article_idx + 1}: {title}")
        print(f"Source: {source}")
        print(f"{'='*80}")
        
        # 1. Meeting occurred
        if result['meeting_occurred']:
            print("\n✓ MEETING OCCURRED:")
            excerpts = find_meeting_excerpts(body)
            print(format_excerpts(excerpts))
        else:
            print("\n✗ MEETING OCCURRED: Not detected")
        
        # 2. Issues discussed
        issues_str = result['issues_discussed']
        if pd.notna(issues_str) and issues_str != 'None':
            print(f"\n✓ ISSUES DISCUSSED: {issues_str}")
            issues_list = [i.strip() for i in issues_str.split(',')]
            for issue in issues_list:
                print(f"\n  Issue: {issue}")
                excerpts = find_issue_excerpts(body, issue)
                print(format_excerpts(excerpts))
        else:
            print("\n✗ ISSUES DISCUSSED: Not detected")
        
        # 3. Questions answered
        if result['questions_answered']:
            print("\n✓ QUESTIONS ANSWERED:")
            excerpts = find_questions_excerpts(body)
            print(format_excerpts(excerpts))
        else:
            print("\n✗ QUESTIONS ANSWERED: Not detected")
        
        # 4. External commentary
        if result['external_commentary']:
            print("\n✓ EXTERNAL COMMENTARY:")
            excerpts = find_commentary_excerpts(body)
            print(format_excerpts(excerpts))
        else:
            print("\n✗ EXTERNAL COMMENTARY: Not detected")
        
        print()  # Blank line between articles
    
    # Summary statistics
    print("\n" + "="*80)
    print("VERIFICATION SUMMARY")
    print("="*80)
    print(f"\nTotal articles reviewed: {len(df_results)}")
    print(f"Articles with meeting mention: {df_results['meeting_occurred'].sum()}")
    print(f"Articles with issues discussed: {df_results[df_results['issues_discussed'] != 'None'].shape[0]}")
    print(f"Articles with questions answered: {df_results['questions_answered'].sum()}")
    print(f"Articles with external commentary: {df_results['external_commentary'].sum()}")
    print("\nReview the excerpts above to verify detection accuracy.")
    print("Look for:")
    print("  - False positives: Detected but excerpt doesn't actually support the message")
    print("  - False negatives: Not detected but should have been")
    print("  - Missing excerpts: Should add more context or refine patterns")


if __name__ == '__main__':
    main()

