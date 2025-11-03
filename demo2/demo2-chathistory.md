# Clone GitHub repository
_Exported on 01/11/2025 at 18:23:21 GMT+8 from Cursor (2.0.43)_

---

**User**

https://github.com/tesolchina/ainewsdemo.git  clone this 

---

**Cursor**


Cloning the repository.


Checking the cloned repository contents:


Repository cloned. Contents:

- **data/** — CSV file (`trump_xi_meeting_fulltext_dedup-1657.csv`)
- **demo/** — Python scripts, requirements, images, and markdown files
- **practice/** — Practice instructions
- **README.md** — Repository readme

Located at `/Users/simonwang/Documents/Usage/aiNews/ainewsdemo/`.

---

**User**

/Users/simonwang/Documents/Usage/aiNews/ainewsdemo/demo2/instructions.md

---

**Cursor**


Reading the instructions file:


Creating a plan markdown file based on the instructions:


Creating the analysis plan markdown file:


```markdown
# Analysis Plan: Key Messages from Trump-Xi Summit News Articles

## Objective
Identify distinct key messages from news articles about the Trump-Xi summit and count how many articles cover each message.

## Input Data
- **File**: `/Users/simonwang/Documents/Usage/aiNews/ainewsdemo/data/trump_xi_meeting_fulltext_dedup-1657.csv`
- **Content**: News articles about the Trump-Xi summit meeting

## Key Message Categories
Based on the research interest, key messages fall into these categories:
1. **Meeting occurred** - Articles mentioning that Trump and Xi met
2. **Issues discussed** - Articles describing specific topics/issues discussed during the meeting
3. **Questions answered** - Articles mentioning questions that were answered
4. **External commentary** - Articles containing comments from other people about the meeting

## Analysis Steps

### Step 1: Data Exploration
- Load and examine the CSV file structure
- Understand the data columns (likely includes article text, source, date, etc.)
- Check data quality (missing values, duplicates, text encoding)
- Get basic statistics (number of articles, date range, sources)

### Step 2: Key Message Extraction
- **Approach**: Use NLP techniques to identify and extract distinct messages
- **Method options**:
  - **Manual review**: Read a sample of articles and manually identify key messages
  - **Keyword-based extraction**: Identify patterns and keywords related to meeting events, discussions, Q&A, and commentary
  - **AI-assisted extraction**: Use language models or topic modeling to identify key themes/messages
  - **Hybrid approach**: Combine automated extraction with manual review

### Step 3: Message Categorization and Standardization
- Create a taxonomy of distinct messages
- Group similar messages (e.g., "discussed trade" and "talked about trade" should map to the same message)
- Define canonical forms for each message type
- Handle variations in wording and paraphrases

### Step 4: Article-to-Message Mapping
- For each article, determine which key messages it covers
- **Approach options**:
  - **Pattern matching**: Use regex or keyword matching to detect messages
  - **Semantic similarity**: Use embeddings/similarity measures to match articles to messages
  - **Classification model**: Train or use a model to classify articles by covered messages
  - **Manual annotation**: Human review of articles (may be necessary for validation)

### Step 5: Counting and Aggregation
- Count how many articles cover each distinct message
- Generate statistics:
  - Total coverage count per message
  - Coverage percentage (articles covering message / total articles)
  - Message frequency distribution
  - Potentially: coverage by date, source, or other dimensions

### Step 6: Output and Visualization
- Create a summary table/matrix showing:
  - List of distinct key messages
  - Coverage count for each message
  - Coverage percentage
  - Examples of articles covering each message (optional)
- Visualizations:
  - Bar chart of message coverage counts
  - Heatmap showing article-to-message coverage matrix (if feasible)
  - Timeline of message coverage (if date information is available)

## Implementation Considerations

### Tools and Libraries
- **Data processing**: pandas for CSV handling
- **Text analysis**: 
  - NLTK or spaCy for NLP processing
  - Regular expressions for pattern matching
  - Sentence transformers or embeddings for semantic matching
- **Visualization**: matplotlib, seaborn, or plotly
- **Optional**: LLM APIs for message extraction and classification

### Challenges to Address
1. **Message granularity**: Determining the right level of detail for messages (too granular vs. too broad)
2. **Synonym handling**: Different phrasings conveying the same message
3. **Implicit vs. explicit**: Messages mentioned directly vs. implied
4. **Message boundaries**: Where one message ends and another begins
5. **Multi-label classification**: Articles can cover multiple messages simultaneously

### Validation Strategy
- Manual review of a sample of articles to verify message extraction
- Inter-annotator agreement if multiple reviewers are used
- Comparison with ground truth if available
- Spot-check of coverage counts

## Expected Deliverables
1. **List of distinct key messages** (with definitions/categories)
2. **Article-to-message mapping** (CSV or structured data)
3. **Coverage statistics** (counts and percentages)
4. **Summary report** (markdown or formatted document)
5. **Visualizations** (charts/graphs as appropriate)
6. **Code/scripts** for reproducibility

```

Created an analysis plan at `/Users/simonwang/Documents/Usage/aiNews/ainewsdemo/demo2/analysis_plan.md`.

The plan includes:
1. Objective and input data
2. Key message categories (meeting, issues discussed, questions answered, external commentary)
3. Six-step process: data exploration → message extraction → categorization → article mapping → counting → output
4. Implementation considerations: tools, challenges, and validation
5. Expected deliverables

Ready for review. Next step: implement the analysis code based on this plan.

---

**User**

/Users/simonwang/Documents/Usage/aiNews/ainewsdemo/demo2/analysis_plan.md

let's not use LLM for now just some NLP tech and try the first 20 articles and check the results 

---

**Cursor**


Updating the plan to exclude LLMs, use NLP only, and test on the first 20 articles. Examining the data structure, then implementing the analysis:


Updating the plan to focus on NLP only and add a test phase, then implementing the analysis:


```markdown
# Analysis Plan: Key Messages from Trump-Xi Summit News Articles

## Objective
Identify distinct key messages from news articles about the Trump-Xi summit and count how many articles cover each message.

## Input Data
- **File**: `/Users/simonwang/Documents/Usage/aiNews/ainewsdemo/data/trump_xi_meeting_fulltext_dedup-1657.csv`
- **Content**: News articles about the Trump-Xi summit meeting

## Key Message Categories
Based on the research interest, key messages fall into these categories:
1. **Meeting occurred** - Articles mentioning that Trump and Xi met
2. **Issues discussed** - Articles describing specific topics/issues discussed during the meeting
3. **Questions answered** - Articles mentioning questions that were answered
4. **External commentary** - Articles containing comments from other people about the meeting

## Analysis Steps

### Step 1: Data Exploration
- Load and examine the CSV file structure
- Understand the data columns (likely includes article text, source, date, etc.)
- Check data quality (missing values, duplicates, text encoding)
- Get basic statistics (number of articles, date range, sources)

### Step 2: Key Message Extraction
- **Approach**: Use NLP techniques (NO LLM APIs) to identify and extract distinct messages
- **Method**:
  - **Initial manual review**: Read first 20 articles and manually identify key messages to create initial taxonomy
  - **Keyword-based extraction**: Identify patterns and keywords related to meeting events, discussions, Q&A, and commentary
  - **Pattern matching**: Use regex patterns to detect common message types
  - **NLP processing**: Use NLTK/spaCy for POS tagging, named entity recognition, and dependency parsing

### Step 3: Message Categorization and Standardization
- Create a taxonomy of distinct messages
- Group similar messages (e.g., "discussed trade" and "talked about trade" should map to the same message)
- Define canonical forms for each message type
- Handle variations in wording and paraphrases

### Step 4: Article-to-Message Mapping
- For each article, determine which key messages it covers
- **Approach options**:
  - **Pattern matching**: Use regex or keyword matching to detect messages
  - **Semantic similarity**: Use embeddings/similarity measures to match articles to messages
  - **Classification model**: Train or use a model to classify articles by covered messages
  - **Manual annotation**: Human review of articles (may be necessary for validation)

### Step 5: Counting and Aggregation
- Count how many articles cover each distinct message
- Generate statistics:
  - Total coverage count per message
  - Coverage percentage (articles covering message / total articles)
  - Message frequency distribution
  - Potentially: coverage by date, source, or other dimensions

### Step 6: Output and Visualization
- Create a summary table/matrix showing:
  - List of distinct key messages
  - Coverage count for each message
  - Coverage percentage
  - Examples of articles covering each message (optional)
- Visualizations:
  - Bar chart of message coverage counts
  - Heatmap showing article-to-message coverage matrix (if feasible)
  - Timeline of message coverage (if date information is available)

## Implementation Considerations

### Tools and Libraries
- **Data processing**: pandas for CSV handling
- **Text analysis**: 
  - NLTK or spaCy for NLP processing
  - Regular expressions for pattern matching
  - Sentence transformers or embeddings for semantic matching
- **Visualization**: matplotlib, seaborn, or plotly
- **Optional**: LLM APIs for message extraction and classification

### Challenges to Address
1. **Message granularity**: Determining the right level of detail for messages (too granular vs. too broad)
2. **Synonym handling**: Different phrasings conveying the same message
3. **Implicit vs. explicit**: Messages mentioned directly vs. implied
4. **Message boundaries**: Where one message ends and another begins
5. **Multi-label classification**: Articles can cover multiple messages simultaneously

### Validation Strategy
- Manual review of a sample of articles to verify message extraction
- Inter-annotator agreement if multiple reviewers are used
- Comparison with ground truth if available
- Spot-check of coverage counts

## Expected Deliverables
1. **List of distinct key messages** (with definitions/categories)
2. **Article-to-message mapping** (CSV or structured data)
3. **Coverage statistics** (counts and percentages)
4. **Summary report** (markdown or formatted document)
5. **Visualizations** (charts/graphs as appropriate)
6. **Code/scripts** for reproducibility


```

```markdown
# Analysis Plan: Key Messages from Trump-Xi Summit News Articles

## Objective
Identify distinct key messages from news articles about the Trump-Xi summit and count how many articles cover each message.

## Input Data
- **File**: `/Users/simonwang/Documents/Usage/aiNews/ainewsdemo/data/trump_xi_meeting_fulltext_dedup-1657.csv`
- **Content**: News articles about the Trump-Xi summit meeting

## Key Message Categories
Based on the research interest, key messages fall into these categories:
1. **Meeting occurred** - Articles mentioning that Trump and Xi met
2. **Issues discussed** - Articles describing specific topics/issues discussed during the meeting
3. **Questions answered** - Articles mentioning questions that were answered
4. **External commentary** - Articles containing comments from other people about the meeting

## Analysis Steps

### Step 1: Data Exploration
- Load and examine the CSV file structure
- Understand the data columns (likely includes article text, source, date, etc.)
- Check data quality (missing values, duplicates, text encoding)
- Get basic statistics (number of articles, date range, sources)

### Step 2: Key Message Extraction
- **Approach**: Use NLP techniques (NO LLM APIs) to identify and extract distinct messages
- **Method**:
  - **Initial manual review**: Read first 20 articles and manually identify key messages to create initial taxonomy
  - **Keyword-based extraction**: Identify patterns and keywords related to meeting events, discussions, Q&A, and commentary
  - **Pattern matching**: Use regex patterns to detect common message types
  - **NLP processing**: Use NLTK/spaCy for POS tagging, named entity recognition, and dependency parsing

### Step 3: Message Categorization and Standardization
- Create a taxonomy of distinct messages
- Group similar messages (e.g., "discussed trade" and "talked about trade" should map to the same message)
- Define canonical forms for each message type
- Handle variations in wording and paraphrases

### Step 4: Article-to-Message Mapping
- For each article, determine which key messages it covers
- **Approach**: 
  - **Pattern matching**: Use regex or keyword matching to detect messages
  - **Keyword-based classification**: Match articles to messages using keyword sets and patterns
  - **NLP features**: Use POS tags, named entities, and sentence structure to identify message types
  - **Manual validation**: Review results on first 20 articles to refine patterns

### Step 5: Counting and Aggregation
- Count how many articles cover each distinct message
- Generate statistics:
  - Total coverage count per message
  - Coverage percentage (articles covering message / total articles)
  - Message frequency distribution
  - Potentially: coverage by date, source, or other dimensions

### Step 6: Output and Visualization
- Create a summary table/matrix showing:
  - List of distinct key messages
  - Coverage count for each message
  - Coverage percentage
  - Examples of articles covering each message (optional)
- Visualizations:
  - Bar chart of message coverage counts
  - Heatmap showing article-to-message coverage matrix (if feasible)
  - Timeline of message coverage (if date information is available)

## Implementation Considerations

### Tools and Libraries
- **Data processing**: pandas for CSV handling
- **Text analysis**: 
  - NLTK or spaCy for NLP processing
  - Regular expressions for pattern matching
  - Sentence transformers or embeddings for semantic matching
- **Visualization**: matplotlib, seaborn, or plotly
- **Optional**: LLM APIs for message extraction and classification

### Challenges to Address
1. **Message granularity**: Determining the right level of detail for messages (too granular vs. too broad)
2. **Synonym handling**: Different phrasings conveying the same message
3. **Implicit vs. explicit**: Messages mentioned directly vs. implied
4. **Message boundaries**: Where one message ends and another begins
5. **Multi-label classification**: Articles can cover multiple messages simultaneously

### Validation Strategy
- Manual review of a sample of articles to verify message extraction
- Inter-annotator agreement if multiple reviewers are used
- Comparison with ground truth if available
- Spot-check of coverage counts

## Expected Deliverables
1. **List of distinct key messages** (with definitions/categories)
2. **Article-to-message mapping** (CSV or structured data)
3. **Coverage statistics** (counts and percentages)
4. **Summary report** (markdown or formatted document)
5. **Visualizations** (charts/graphs as appropriate)
6. **Code/scripts** for reproducibility


```

```markdown
# Analysis Plan: Key Messages from Trump-Xi Summit News Articles

## Objective
Identify distinct key messages from news articles about the Trump-Xi summit and count how many articles cover each message.

## Input Data
- **File**: `/Users/simonwang/Documents/Usage/aiNews/ainewsdemo/data/trump_xi_meeting_fulltext_dedup-1657.csv`
- **Content**: News articles about the Trump-Xi summit meeting

## Key Message Categories
Based on the research interest, key messages fall into these categories:
1. **Meeting occurred** - Articles mentioning that Trump and Xi met
2. **Issues discussed** - Articles describing specific topics/issues discussed during the meeting
3. **Questions answered** - Articles mentioning questions that were answered
4. **External commentary** - Articles containing comments from other people about the meeting

## Analysis Steps

### Step 1: Data Exploration
- Load and examine the CSV file structure
- Understand the data columns (likely includes article text, source, date, etc.)
- Check data quality (missing values, duplicates, text encoding)
- Get basic statistics (number of articles, date range, sources)

### Step 2: Key Message Extraction
- **Approach**: Use NLP techniques (NO LLM APIs) to identify and extract distinct messages
- **Method**:
  - **Initial manual review**: Read first 20 articles and manually identify key messages to create initial taxonomy
  - **Keyword-based extraction**: Identify patterns and keywords related to meeting events, discussions, Q&A, and commentary
  - **Pattern matching**: Use regex patterns to detect common message types
  - **NLP processing**: Use NLTK/spaCy for POS tagging, named entity recognition, and dependency parsing

### Step 3: Message Categorization and Standardization
- Create a taxonomy of distinct messages
- Group similar messages (e.g., "discussed trade" and "talked about trade" should map to the same message)
- Define canonical forms for each message type
- Handle variations in wording and paraphrases

### Step 4: Article-to-Message Mapping
- For each article, determine which key messages it covers
- **Approach**: 
  - **Pattern matching**: Use regex or keyword matching to detect messages
  - **Keyword-based classification**: Match articles to messages using keyword sets and patterns
  - **NLP features**: Use POS tags, named entities, and sentence structure to identify message types
  - **Manual validation**: Review results on first 20 articles to refine patterns

### Step 5: Counting and Aggregation
- Count how many articles cover each distinct message
- Generate statistics:
  - Total coverage count per message
  - Coverage percentage (articles covering message / total articles)
  - Message frequency distribution
  - Potentially: coverage by date, source, or other dimensions

### Step 6: Output and Visualization
- Create a summary table/matrix showing:
  - List of distinct key messages
  - Coverage count for each message
  - Coverage percentage
  - Examples of articles covering each message (optional)
- Visualizations:
  - Bar chart of message coverage counts
  - Heatmap showing article-to-message coverage matrix (if feasible)
  - Timeline of message coverage (if date information is available)

## Implementation Considerations

### Tools and Libraries
- **Data processing**: pandas for CSV handling
- **Text analysis**: 
  - NLTK or spaCy for NLP processing (tokenization, POS tagging, NER)
  - Regular expressions for pattern matching
  - Keyword-based matching (no LLM/embeddings needed)
- **Visualization**: matplotlib, seaborn, or plotly
- **Note**: NO LLM APIs - using traditional NLP techniques only

### Testing Strategy
- **Phase 1**: Test on first 20 articles
  - Extract and identify key messages manually
  - Develop pattern matching rules
  - Validate results manually
  - Refine approach based on findings
- **Phase 2**: Scale to full dataset after validation

### Challenges to Address
1. **Message granularity**: Determining the right level of detail for messages (too granular vs. too broad)
2. **Synonym handling**: Different phrasings conveying the same message
3. **Implicit vs. explicit**: Messages mentioned directly vs. implied
4. **Message boundaries**: Where one message ends and another begins
5. **Multi-label classification**: Articles can cover multiple messages simultaneously

### Validation Strategy
- Manual review of a sample of articles to verify message extraction
- Inter-annotator agreement if multiple reviewers are used
- Comparison with ground truth if available
- Spot-check of coverage counts

## Expected Deliverables
1. **List of distinct key messages** (with definitions/categories)
2. **Article-to-message mapping** (CSV or structured data)
3. **Coverage statistics** (counts and percentages)
4. **Summary report** (markdown or formatted document)
5. **Visualizations** (charts/graphs as appropriate)
6. **Code/scripts** for reproducibility


```

Creating a Python script to analyze the first 20 articles using NLP techniques:


Creating a Python script to analyze the first 20 articles:


```python
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
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger', quiet=True)

try:
    nltk.data.find('chunkers/maxent_ne_chunker')
except LookupError:
    nltk.download('maxent_ne_chunker', quiet=True)
    nltk.download('words', quiet=True)


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
    
    if has_commentary and has_commentator:
        # Try to extract named entities for commentators
        sentences = sent_tokenize(text)
        for sentence in sentences[:10]:  # Check first 10 sentences
            if any(keyword in sentence.lower() for keyword in ['said', 'commented', 'noted', 'stated']):
                # Check if sentence mentions officials/analysts
                if any(indicator in sentence.lower() for indicator in ['official', 'analyst', 'expert', 'spokesperson']):
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

```

Creating a requirements file and running the script:


```pip-requirements
pandas>=2.2.2
nltk>=3.8.1

```

Simplifying the script to avoid NLTK download issues by using simpler text processing:


```python
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
    
    if has_commentary and has_commentator:
        # Try to extract named entities for commentators
        sentences = sent_tokenize(text)
        for sentence in sentences[:10]:  # Check first 10 sentences
            if any(keyword in sentence.lower() for keyword in ['said', 'commented', 'noted', 'stated']):
                # Check if sentence mentions officials/analysts
                if any(indicator in sentence.lower() for indicator in ['official', 'analyst', 'expert', 'spokesperson']):
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


```

```python
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


```

Script ran successfully. Checking the results and generating a summary report:


Creating a summary report:


```markdown
# Key Message Extraction Report - First 20 Articles

## Analysis Summary

This report presents the results of extracting key messages from the first 20 news articles about the Trump-Xi summit meeting using NLP techniques (regex patterns and keyword matching).

**Input File**: `trump_xi_meeting_fulltext_dedup-1657.csv`  
**Articles Analyzed**: 20 (first 20 from dataset)  
**Method**: Pattern matching, keyword-based extraction (NO LLM)

---

## Key Message Categories Coverage

### 1. Meeting Occurred
- **Articles covering**: 13 / 20 (65.0%)
- **Description**: Articles that explicitly mention that Trump and Xi met

### 2. Issues Discussed
- **Articles mentioning issues**: 11 / 20 (55.0%)
- **Description**: Articles that discuss specific topics/issues during the meeting

**Top Issues Identified:**
| Issue | Coverage Count |
|-------|----------------|
| trade | 10 articles |
| north korea | 6 articles |
| technology | 4 articles |
| taiwan | 2 articles |
| ip rights | 2 articles |
| hong kong | 2 articles |
| south china sea | 1 article |

### 3. Questions Answered
- **Articles covering**: 1 / 20 (5.0%)
- **Description**: Articles mentioning that questions were answered during the meeting

### 4. External Commentary
- **Articles covering**: 14 / 20 (70.0%)
- **Description**: Articles containing comments from other people (officials, analysts, experts) about the meeting

---

## Detailed Article-by-Article Results

The following table shows which messages each article covers:

| # | Title | Source | Meeting | Issues | Q&A | Commentary |
|---|-------|--------|---------|--------|-----|------------|
| 1 | APEC summit to close in South Korea after Trump, Xi agreed on trade truce | Winnipeg Free Press | ✓ | trade, north korea | | ✓ |
| 2 | China's Xi in the spotlight at Pacific summit while Trump is conspicuous... | ExBulletin | ✓ | trade, north korea, technology, taiwan | | ✓ |
| 3 | APEC summit to close in South Korea after Trump, Xi agreed on trade truce | WTOP | ✓ | trade, north korea, ip rights | | ✓ |
| 4 | @ the Bell: Tariffs and treats -- Trump and Xi call a truce... | stockhouse | ✓ | | | |
| 5 | Trump may have skipped APEC, but Xi is using it to sell China... | ExBulletin | | | | |
| 6 | APEC Summit: Trump's Truce with Xi Steals the Limelight | Devdiscourse | | trade, north korea | | |
| 7 | Trump and Xi pause trade war, not rivalry | The Tribune | ✓ | trade, taiwan, north korea, south china sea, technology | | ✓ |
| 8 | Analysis: China's Xi has the advantage after his trade meeting with Trump | ExBulletin | | | | ✓ |
| 9 | VIDEO: Trump dan Xi Jinping Sepakat Akhiri Ketegangan Dagang! | CNNindonesia | | | | |
| 10 | APEC summit to close in South Korea after Trump, Xi agreed on trade... | Daily Mail Online | ✓ | trade, north korea | | ✓ |
| 11 | Nvidia Uncertain if Return to China Is Closer After Trump-Xi Meeting | The New York Times | ✓ | technology | | ✓ |
| 12 | White House releases relaxed images from Xi-Trump summit in Busan | Dimsum Daily | ✓ | | | ✓ |
| 13 | Trump not discussing Russia oil sanctions with Xi signals priorities shift | Pravda EN | | | | ✓ |
| 14 | White House official: Trump spoke with Xi Jinping about Jimmy Lai's release | Catholic News Agency | | | | ✓ |
| 15 | Trump-Xi meeting: Shaping future of US-China ties | Pakistan Observer | ✓ | trade, hong kong | | ✓ |
| 16 | Trump-Xi talks didn't change Beijing's priority: flagging economy | Inside The Star-Studded World | ✓ | trade, ip rights, technology | | ✓ |
| 17 | Trump, Xi consider deal to ease US-China trade war, but tensions remain | ExBulletin | ✓ | | | ✓ |
| 18 | As Trump skips APEC, China's Xi fills the void with message on trade | The Straits Times | ✓ | trade | | ✓ |
| 19 | HONG KONG - CHINA Human rights and freedom missing from the Trump-Xi summit | Asia News.it | ✓ | trade, hong kong | ✓ | |
| 20 | Chinese Exporters Bet That Xi-Trump Tariff Truce Won't Last | news.bloomberglaw.com | | | | |

---

## Observations and Findings

1. **Meeting Mention Coverage**: 65% of articles explicitly mention the meeting occurred, which suggests some articles focus on implications rather than the event itself.

2. **Issue Discussion**: Trade is the most frequently discussed issue (10 articles), followed by North Korea (6 articles). This aligns with the summit's focus on trade tensions.

3. **Questions Answered**: Very low coverage (5%), suggesting most articles don't focus on Q&A aspects of the meeting.

4. **External Commentary**: High coverage (70%), indicating most articles include perspectives from officials, analysts, or experts rather than just reporting facts.

5. **Multi-message Articles**: Many articles cover multiple messages simultaneously. For example, Article 7 covers meeting, multiple issues, and external commentary.

---

## Method Details

### Detection Patterns Used

1. **Meeting Occurred**:
   - Patterns like "Trump/Xi met", "Trump-Xi meeting", "summit", "talks"
   - Regex patterns checking for meeting verbs within proximity of names

2. **Issues Discussed**:
   - Keyword matching for specific issues (trade, north korea, technology, etc.)
   - Detection of discussion verbs (discussed, talked about, addressed, etc.)
   - Combined pattern: discussion verb + issue keyword

3. **Questions Answered**:
   - Patterns like "answered questions", "Q&A", "responded to questions"
   - Question-answer verb combinations

4. **External Commentary**:
   - Commentary verbs (said, commented, noted, stated)
   - Commentator indicators (official, analyst, expert, spokesperson)
   - Both must be present to detect external commentary

### Limitations

- Pattern matching may miss implicit messages
- Synonym handling is basic (may miss variations)
- False positives/negatives possible - manual validation recommended
- Only tested on 20 articles - patterns may need refinement for full dataset

---

## Next Steps

1. **Manual Validation**: Review a sample of results to verify accuracy
2. **Pattern Refinement**: Adjust regex patterns based on false positives/negatives
3. **Scale Up**: Apply to full dataset (1657 articles) after validation
4. **Enhanced Extraction**: Consider more sophisticated NLP for better synonym handling
5. **Message Standardization**: Create canonical forms for similar messages

---

**Generated by**: `extract_key_messages.py`  
**Date**: Analysis run on first 20 articles  
**Results CSV**: `message_extraction_results.csv`

```

Checking for linting issues:


## Summary

1. **Updated the analysis plan** (`analysis_plan.md`) to:
   - Remove LLM references
   - Focus on NLP techniques (regex patterns, keyword matching)
   - Add a testing strategy starting with the first 20 articles

2. **Created and ran the analysis script** (`extract_key_messages.py`):
   - Uses regex patterns and keyword matching (no LLM)
   - Processes the first 20 articles
   - Extracts 4 key message types

3. **Results from first 20 articles**:
   - **Meeting occurred**: 13/20 (65%)
   - **Issues discussed**: 11/20 (55%) — trade is most common (10 articles)
   - **Questions answered**: 1/20 (5%)
   - **External commentary**: 14/20 (70%)

4. **Generated outputs**:
   - `message_extraction_results.csv` — detailed article-by-article results
   - `message_extraction_report.md` — analysis report with findings
   - `requirements.txt` — dependencies

The script uses pattern matching and keyword detection. Results are saved to CSV and the markdown report for review. You can validate the results and refine the patterns before scaling to the full dataset.

Should I review specific articles to validate the extraction, or adjust the detection patterns?

---

**User**

but we need to verify the results 

can you generate a new python file to show the excerpts that support the identified items 

---

**Cursor**


Creating a script to extract and display excerpts supporting each detected message for verification:


Creating a script to extract and display excerpts supporting each detected message:


```python
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

```

Running the verification script to show supporting excerpts:


Saving the verification output to a file for review:


Verification script created and executed. Reviewing the end of the output for a summary:


Checking for potential false positives (detected but no supporting excerpts found):


Created a verification script. Summary:

## Created: `verify_extractions.py`

This script:
1. Loads the article data and extraction results
2. For each detected message, finds and displays supporting text excerpts
3. Shows which parts of the article text triggered each detection
4. Highlights potential false positives (detected but no excerpts found)

## Output

The verification results are saved to `verification_output.txt` (536 lines). It shows:
- For each article: which messages were detected and the excerpts that support them
- Cases where no excerpts were found (potential false positives)
- A summary at the end

## Findings from verification

The script found several cases where issues were detected but no supporting excerpts were found:
- Article 2: "north korea" and "technology" detected but no excerpts
- Article 3: "ip rights" detected but no excerpts
- Some articles: "taiwan" and "south china sea" detected but no excerpts

This suggests the detection patterns may need refinement — keywords may appear without clear evidence that they were discussed between Trump and Xi.

You can:
1. Review the full verification output: `verification_output.txt`
2. Use the script anytime: `python3 verify_extractions.py`
3. Refine the patterns in `extract_key_messages.py` based on what you see

Should I refine the detection patterns to reduce these false positives?

---

**User**

I need a smaller sample 

maybe just 5 articles full texts with URL and the analysis results 

then I can identify the problems 

---

**Cursor**


Creating a script to generate a focused report for 5 articles with full text, URLs, and analysis results:


```python
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
        article_idx = int(result['article_idx'])
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

```

Fixing a bug in the script:


```python
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


```

Previewing the sample output:


Created two files with 5 sample articles for review:

## Generated files

1. `sample_articles_review.txt` — plain text format
2. `sample_articles_review.md` — markdown format (easier to read in a text editor)

## Contents

Each file includes all 5 articles with:
- **Title**
- **Source**
- **Published date**
- **URL**
- **Analysis results** (what was detected):
  - Meeting Occurred: ✓/✗
  - Issues Discussed: list
  - Questions Answered: ✓/✗
  - External Commentary: ✓/✗
- **Full article text**

## Review

Use these files to:
1. Read each article’s full text
2. Check the analysis results
3. Identify issues:
   - False positives (detected incorrectly)
   - False negatives (missed items)
   - Issues listed without clear evidence they were discussed

For example, Article 2 shows "north korea, technology, trade, taiwan" as issues discussed — verify if the text supports these.

Files are ready in the `demo2` folder.

