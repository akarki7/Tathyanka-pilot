"""
https://huggingface.co/mrm8488/t5-base-finetuned-wikiSQL?text=translate+English+to+SQL%3A+How+many+models+were+finetuned+using+BERT+as+base+model%3F

"""

from transformers import AutoModelWithLMHead, AutoTokenizer
from datasets import load_dataset, Split
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-wikiSQL")
model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-wikiSQL")


def get_sql(query):
    input_text = "translate English to SQL: %s </s>" % query
    features = tokenizer([input_text], return_tensors="pt")

    output = model.generate(
        input_ids=features["input_ids"], attention_mask=features["attention_mask"]
    )
    return tokenizer.decode(output[0])


# query1 = "Deposit by bank type"
# query2 = "How many players from the United States play PG?"
# query3 = "The deposit of last 10 month?"

# if "deposit" or "Deposit" in query3:
#     result = get_sql(query3)
#     result = result.replace("table", "deposit")
#     print(result)


# print(get_sql(query3))

valid_dataset = load_dataset("wikisql", split=Split.VALIDATION)
print(valid_dataset[500])
