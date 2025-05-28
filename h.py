from transformers import AutoModel, AutoTokenizer, AutoModelForQuestionAnswering, pipeline

model_name = "microsoft/layoutlmv3-large" #"impira/layoutlm-document-qa"
# model = AutoModelForQuestionAnswering.from_pretrained("microsoft/layoutlmv3-large")
# print(model)
# model_name = "microsoft/layoutlmv3-base" 
# qa_pipeline = pipeline("question-answering", model=model_name, tokenizer=model_name)
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

result = qa_pipeline({
    "question": "What is the date of today?",
    "context": "todays date is 2023-10-01. This document was created on 2023-march-30."
})

print(result["answer"])
