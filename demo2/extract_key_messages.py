#!/usr/bin/env python3
"""
Extract key messages from Trump-Xi summit news articles using NLP techniques.

This script:
1. Loads the first 20 articles from the CSV
2. Uses NLP (no LLM) to identify key messages
3. Maps articles to messages
4. Counts coverage statistics
"""

import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Set, Tuple

import pandas as pd


def normalize_text(text: str) -> str:
    """Normalize text for processing."""
    if pd.isna(text):
        return ""
    return str(text).lower()


def find_meeting_mentions(text: str) -> bool:
    """Check if article mentions that Trump and Xi met."""
    text_lower = normalize_text(text)
    
    # Patterns indicating meeting occurred
    patterns = [
        r'\b(trump|donald trump|president trump).{0,50}(met|meeting|met with|met up|gathered|sat down|held.{0,20}meeting|had.{0,20}meeting)',
        r'\b(xi|xi jinping|president xi).{0,50}(met|meeting|met with|met up|gathered|sat down|held.{0,20}meeting|had.{0,20}meeting)',
        r'\b(trump.{0,30}xi|xi.{0,30}trump).{0,20}(meeting|summit|talks|encounter)',
        r'\b(trump-xi|xi-trump).{0,20}(meeting|summit)',
    ]
    
    for pattern in patterns:
        if re.search(pattern, text_lower, re.IGNORECASE):
            return True
    return False


def find_issues_discussed(text: str) -> List[str]:
    """Extract specific issues/topics discussed."""
    text_lower = normalize_text(text)
    issues = []
    
    # Common issue keywords
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
    
    # Patterns for discussion
    discussion_patterns = [
        r'\b(discussed|talked about|talked|spoke about|addressed|covered|focused on|centered on|revolved around|dealt with)',
        r'\b(conversation|discussion|talks|dialogue).{0,30}(about|on|regarding|concerning)',
    ]
    
    # Check if any discussion pattern exists
    has_discussion = any(re.search(pattern, text_lower, re.IGNORECASE) for pattern in discussion_patterns)
    
    if has_discussion:
        for issue_name, keywords in issue_keywords.items():
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower, re.IGNORECASE):
                    issues.append(issue_name)
                    break
    
    return list(set(issues))  # Remove duplicates


def find_questions_answered(text: str) -> bool:
    """Check if article mentions questions being answered."""
    text_lower = normalize_text(text)
    
    patterns = [
        r'\b(answered|responded|replied).{0,30}(question|questions|query|queries)',
        r'\b(question|questions).{0,30}(answered|responded|addressed|addressing)',
        r'\b(q&a|q and a|question.{0,20}answer)',
        r'\b(asked|asking).{0,30}(trump|xi|president).{0,50}(answered|responded|said|replied)',
    ]
    
    return any(re.search(pattern, text_lower, re.IGNORECASE) for pattern in patterns)


def find_external_commentary(text: str) -> List[str]:
    """Find mentions of other people commenting on the meeting."""
    text_lower = normalize_text(text)
    commentators = []
    
    # Patterns for commentary
    commentary_patterns = [
        r'\b(said|stated|commented|remarked|noted|observed|suggested|indicated|expressed|claimed|added)',
        r'\b(according to|as.{0,20}said|quoted.{0,20}as.{0,20}saying)',
    ]
    
    # Common commentator indicators
    commentator_indicators = [
        r'\b(analyst|expert|official|spokesperson|spokesman|spokeswoman|minister|secretary|ambassador)',
        r'\b(white house|state department|chinese.{0,20}foreign.{0,20}ministry)',
    ]
    
    has_commentary = any(re.search(pattern, text_lower, re.IGNORECASE) for pattern in commentary_patterns)
    has_commentator = any(re.search(pattern, text_lower, re.IGNORECASE) for pattern in commentator_indicators)
    
    # Simple sentence splitting for checking
    if has_commentary and has_commentator:
        # Split by sentence endings
        sentences = re.split(r'[.!?]+\s+', text)
        for sentence in sentences[:10]:  # Check first 10 sentences
            sentence_lower = sentence.lower()
            if any(keyword in sentence_lower for keyword in ['said', 'commented', 'noted', 'stated']):
                # Check if sentence mentions officials/analysts
                if any(indicator in sentence_lower for indicator in ['official', 'analyst', 'expert', 'spokesperson']):
                    return ['external_commentary_detected']
    
    return ['external_commentary_detected'] if (has_commentary and has_commentator) else []


def extract_messages_from_article(body: str) -> Dict[str, any]:
    """Extract all key messages from an article."""
    if pd.isna(body) or not body:
        return {
            'meeting_occurred': False,
            'issues_discussed': [],
            'questions_answered': False,
            'external_commentary': []
        }
    
    messages = {
        'meeting_occurred': find_meeting_mentions(body),
        'issues_discussed': find_issues_discussed(body),
        'questions_answered': find_questions_answered(body),
        'external_commentary': find_external_commentary(body)
    }
    
    return messages


def main():
    input_file = Path(__file__).parent.parent / 'data' / 'trump_xi_meeting_fulltext_dedup-1657.csv'
    
    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}", file=sys.stderr)
        sys.exit(1)
    
    # Load data
    print(f"Loading data from {input_file}...")
    df = pd.read_csv(input_file)
    print(f"Total articles: {len(df)}")
    
    # Process first 20 articles
    df_subset = df.head(20).copy()
    print(f"\nProcessing first 20 articles...")
    
    # Extract messages
    results = []
    for idx, row in df_subset.iterrows():
        messages = extract_messages_from_article(row['body'])
        results.append({
            'index': idx,
            'title': row['title'],
            'source': row['source'],
            'meeting_occurred': messages['meeting_occurred'],
            'issues_discussed': ', '.join(messages['issues_discussed']) if messages['issues_discussed'] else 'None',
            'num_issues': len(messages['issues_discussed']),
            'questions_answered': messages['questions_answered'],
            'external_commentary': bool(messages['external_commentary']),
        })
    
    # Create results dataframe
    results_df = pd.DataFrame(results)
    
    # Count statistics
    print("\n" + "="*80)
    print("KEY MESSAGE COVERAGE STATISTICS (First 20 Articles)")
    print("="*80)
    
    total_articles = len(results_df)
    
    print(f"\n1. Meeting Occurred:")
    print(f"   Articles covering: {results_df['meeting_occurred'].sum()} / {total_articles} ({100*results_df['meeting_occurred'].sum()/total_articles:.1f}%)")
    
    print(f"\n2. Issues Discussed:")
    all_issues = []
    for issues_str in results_df['issues_discussed']:
        if issues_str != 'None':
            all_issues.extend(issues_str.split(', '))
    issue_counts = pd.Series(all_issues).value_counts()
    print(f"   Articles mentioning issues: {results_df[results_df['issues_discussed'] != 'None'].shape[0]} / {total_articles}")
    if len(issue_counts) > 0:
        print(f"   Top issues discussed:")
        for issue, count in issue_counts.head(10).items():
            print(f"     - {issue}: {count} articles")
    
    print(f"\n3. Questions Answered:")
    print(f"   Articles covering: {results_df['questions_answered'].sum()} / {total_articles} ({100*results_df['questions_answered'].sum()/total_articles:.1f}%)")
    
    print(f"\n4. External Commentary:")
    print(f"   Articles covering: {results_df['external_commentary'].sum()} / {total_articles} ({100*results_df['external_commentary'].sum()/total_articles:.1f}%)")
    
    # Save detailed results
    output_file = Path(__file__).parent / 'message_extraction_results.csv'
    results_df.to_csv(output_file, index=False)
    print(f"\nDetailed results saved to: {output_file}")
    
    # Show sample articles
    print("\n" + "="*80)
    print("SAMPLE ARTICLES WITH MESSAGES")
    print("="*80)
    for i, result in enumerate(results[:5], 1):
        print(f"\nArticle {i}: {result['title'][:80]}...")
        print(f"  Source: {result['source']}")
        print(f"  Meeting occurred: {result['meeting_occurred']}")
        print(f"  Issues discussed: {result['issues_discussed']}")
        print(f"  Questions answered: {result['questions_answered']}")
        print(f"  External commentary: {result['external_commentary']}")


if __name__ == '__main__':
    main()

