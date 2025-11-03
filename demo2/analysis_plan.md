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

