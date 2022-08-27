import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


class AIkash:

    def __init__(self,
                 device='cpu',
                 model_path='ruDialoGPT-medium',
                 num_threads=None):

        self.device = torch.device(device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path).to(device)
        if num_threads: torch.set_num_threads(num_threads)
        #if self.device != 'cpu': self.model.cuda()

    def __post_init__(self):
        pass

    def work(self, text_):

        input_ids = self.tokenizer.encode(text_, return_tensors="pt").to(self.device)
        out = self.model.generate(
            input_ids,
            top_k=10,
            top_p=0.95,
            num_beams=3,
            num_return_sequences=3,
            do_sample=True,
            no_repeat_ngram_size=2,
            temperature=1.2,
            repetition_penalty=1.2,
            length_penalty=1.0,
            eos_token_id=50257,
            max_new_tokens=40
        )
        res = list(map(self.tokenizer.decode, out))[0]
        res_text = (res.split("@@ПЕРВЫЙ@@")[0]).split("@@ВТОРОЙ@@")[-1]
        print(f"{text_} ----> {res_text}")
        return res_text
