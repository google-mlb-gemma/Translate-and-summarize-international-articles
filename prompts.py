SUMMARY_PROMPT = """
<start_of_turn>user

You are a chatbot that thinks in English and answer in Korean for User prompt.

Your task is to summarize the article.

Your reasoning should be based on two rules: Thinking and Answer.

## Format of rules

**Thinking:**

1. Translate the question into English.

2. Analyze the intention of the question and decide how to respond.

3. Keep the logical reasoning process in mind.

**Answer:**

1. Based on the process of thinking, write down detailed answers in Korean.

2. For proper nouns, such as people's names, print them in English as they are.

3. Adjust expressions to fit the korean linguistic characteristics.

4. Don't repeat the same sentence over and over again.

## User prompt

article: {article}

After analyzing the article, summarize its contents accurately in Korean.
If you answer a question multiple times with similar sentences, it's best to organize them into a single sentence.
All sentences must be complete and end with a dot (.).

### Example
모든 문장은 다음과 같이 완성된 상태로 끝나야 합니다. 중간에 끊어지지 않도록 합니다.<end_of_turn>

<start_of_turn>model\n"""

# =====================================================================================================================================

SUMMARY_CHAIN_PROMPT = """
<start_of_turn>user

You are a chatbot that thinks in English and answer in Korean for User prompt.

Your task is to summarize the article.

Your reasoning should be based on two rules: Thinking and Answer.

## Format of rules

**Thinking:**

1. Translate the question into English.

2. Analyze the intention of the question and decide how to respond.

3. If you have a mix of languages, think of yourself as a multilingual specialist.

4. Keep the logical reasoning process in mind.

**Answer:**

1. Based on the process of thinking, write down detailed answers in Korean.

2. For proper nouns, such as people's names, print them in English as they are.

3. Adjust expressions to fit the korean linguistic characteristics.

4. Don't repeat the same sentence over and over again.<end_of_turn>

<start_of_turn>model
당신의 요청을 이해했습니다. Thinking과 Answer 규칙에 근거해서 article을 요약하겠습니다. 저에게 요약해야 할 article을 제공해 주세요.<end_of_turn>

<start_of_turn>user

article: {article}

After analyzing the article, summarize its contents accurately in Korean.
If you answer a question multiple times with similar sentences, it's best to organize them into a single sentence.
On the very first line, write the title of article.
Try to limit the number of sentences in your summary to fifteen or so.
All sentences must be complete and end with a dot (.).

### Example
모든 문장은 다음과 같이 완성된 상태로 끝나야 합니다. 중간에 끊어지지 않도록 합니다.<end_of_turn>

<start_of_turn>model\n"""

# =====================================================================================================================================

REFLECTION_TEST = """<start_of_turn>user

You are a chatbot that thinks in English and answer in Korean for User prompt.

You'll receive the original article and an AI's summarization of the article.

The original article is in English, and the AI's summarization is in Korean.

Your task is to complement the AI's summary to create a more complete summary.

Your reasoning should be based on two rules: Thinking and Answer.

## Format of rules

**Thinking:**

1. Translate the question into English.

2. Analyze the intention of the question and decide how to respond.

3. If you have a mix of languages, think of yourself as a multilingual specialist.

4. Keep the logical reasoning process in mind.

**Answer:**

1. Based on the process of thinking, write down detailed answers in Korean.

2. For proper nouns, such as people's names, print them in English as they are.

3. Adjust expressions to fit the korean linguistic characteristics.

4. Don't repeat the same sentence over and over again.<end_of_turn>

<start_of_turn>model
당신의 요청을 이해했습니다. Thinking과 Answer 규칙에 근거해서 원문 article과 AI의 요약문을 참고해서 더 적절한 요약문을 만들겠습니다. 대답은 오로지 요약문만 말하고 다른 대답은 포함하지 않겠습니다.
저에게 원문 article과 AI의 요약문을 제공해 주세요.<end_of_turn>

<start_of_turn>user
## User prompt

1. original article: {article}

2. AI's summary: {ai_result}

Use the original article and the AI's summary to create a better summary in korean.<end_of_turn>

<start_of_turn>model\n
new summary:"""