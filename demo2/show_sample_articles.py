#!/usr/bin/env python3
"""
Generate a focused sample report showing 5 articles with full text, URLs, and analysis results.

This provides a manageable sample for manual review to identify detection problems.
"""

import sys
from pathlib import Path

import pandas as pd


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
    
    # Select first 5 articles
    sample_size = 5
    df_sample = df_results.head(sample_size).copy()
    
    # Generate report
    output_lines = []
    output_lines.append("="*80)
    output_lines.append("SAMPLE ARTICLES WITH FULL TEXT AND ANALYSIS RESULTS")
    output_lines.append("="*80)
    output_lines.append(f"\nShowing first {sample_size} articles for manual review\n")
    
    for idx, result in df_sample.iterrows():
        article_idx = int(result['index'])
        article = df_articles.iloc[article_idx]
        
        title = article['title']
        source = article['source']
        url = article['url'] if pd.notna(article['url']) else "N/A"
        published = article['published'] if pd.notna(article['published']) else "N/A"
        body = article['body'] if pd.notna(article['body']) else ""
        
        output_lines.append("\n" + "="*80)
        output_lines.append(f"ARTICLE {idx + 1} / {sample_size}")
        output_lines.append("="*80)
        output_lines.append(f"\nTitle: {title}")
        output_lines.append(f"Source: {source}")
        output_lines.append(f"Published: {published}")
        output_lines.append(f"URL: {url}")
        output_lines.append("\n" + "-"*80)
        output_lines.append("ANALYSIS RESULTS:")
        output_lines.append("-"*80)
        output_lines.append(f"\n1. Meeting Occurred: {'✓ YES' if result['meeting_occurred'] else '✗ NO'}")
        output_lines.append(f"2. Issues Discussed: {result['issues_discussed'] if result['issues_discussed'] != 'None' else 'None detected'}")
        output_lines.append(f"3. Questions Answered: {'✓ YES' if result['questions_answered'] else '✗ NO'}")
        output_lines.append(f"4. External Commentary: {'✓ YES' if result['external_commentary'] else '✗ NO'}")
        output_lines.append("\n" + "-"*80)
        output_lines.append("FULL ARTICLE TEXT:")
        output_lines.append("-"*80)
        output_lines.append(f"\n{body}")
        output_lines.append("\n" + "="*80)
        output_lines.append("")  # Blank line between articles
    
    # Save to file
    output_file = Path(__file__).parent / 'sample_articles_review.txt'
    output_text = "\n".join(output_lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text)
    
    print(f"\nSample report saved to: {output_file}")
    print(f"\nArticles included:")
    for idx, result in df_sample.iterrows():
        article_idx = int(result['index'])
        title = df_articles.iloc[article_idx]['title']
        print(f"  {idx + 1}. {title[:70]}...")
    
    # Also create a markdown version
    md_lines = []
    md_lines.append("# Sample Articles Review - First 5 Articles")
    md_lines.append("\nThis document contains full article texts with analysis results for manual review.")
    md_lines.append("\n---\n")
    
    for idx, result in df_sample.iterrows():
        article_idx = int(result['index'])
        article = df_articles.iloc[article_idx]
        
        title = article['title']
        source = article['source']
        url = article['url'] if pd.notna(article['url']) else "N/A"
        published = article['published'] if pd.notna(article['published']) else "N/A"
        body = article['body'] if pd.notna(article['body']) else ""
        
        md_lines.append(f"\n## Article {idx + 1}: {title}\n")
        md_lines.append(f"**Source**: {source}  ")
        md_lines.append(f"**Published**: {published}  ")
        md_lines.append(f"**URL**: {url}")
        md_lines.append("\n### Analysis Results\n")
        md_lines.append(f"- **Meeting Occurred**: {'✓ YES' if result['meeting_occurred'] else '✗ NO'}")
        issues = result['issues_discussed'] if result['issues_discussed'] != 'None' else 'None'
        md_lines.append(f"- **Issues Discussed**: {issues}")
        md_lines.append(f"- **Questions Answered**: {'✓ YES' if result['questions_answered'] else '✗ NO'}")
        md_lines.append(f"- **External Commentary**: {'✓ YES' if result['external_commentary'] else '✗ NO'}")
        md_lines.append("\n### Full Article Text\n")
        md_lines.append("```")
        md_lines.append(body)
        md_lines.append("```")
        md_lines.append("\n---\n")
    
    md_file = Path(__file__).parent / 'sample_articles_review.md'
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(md_lines))
    
    print(f"Markdown version saved to: {md_file}")


if __name__ == '__main__':
    main()

