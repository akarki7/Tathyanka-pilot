from transformers import AutoModelWithLMHead, AutoTokenizer
from datasets import load_dataset
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
