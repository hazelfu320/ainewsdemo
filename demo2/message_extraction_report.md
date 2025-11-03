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

