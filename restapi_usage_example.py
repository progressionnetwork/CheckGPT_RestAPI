import json
import requests

url = "http://checkgpt.app:8880/predict"

data_empl = {
    "text": """In the one point of view, it is one of the man’s characters to be curious. He wants to break the limits and learn more. No one can oppose to this quality of human. This curiosity caused many inventions and profits for the people around the world. In the other hand, we live together and we should think about others, have compassion for them and give their due. It is not fair that governments notice on their points and don’t think that it may harm other people. In my opinion, governments should spend money for our basic needs on earth and stop spending money for outer space researches.
If one person deprived himself and his family from eating to buy and run a car, we may consider him mad. It is not acceptable to spend millions of money’s funds and expenditures for space researches while there are many people around the world who have a severe lack of food, water, and hygiene and many other primary necessities. When we see that there is many violent thugs, suicides, robberies and divorces occur in our society and most of these problems are because of lack of money or poverty, It is not conventional to squander this huge amount of money for traveling to space while many essential requirements have not answered yet.
Many times, we see from our television or read from news that our earth is in a very bad condition. Deforesting caused many jungles destroyed; air pollution is going to be a very dangerous problem and so on. It is utterly absurd that governments waste this amount of money while our earth, the only place for us to live; situation deteriorates every day so fast.
At last but not the least, there are still many troubles in our society and earth in that many people die because of lack of food and water supply in the 20th century what is not a negligible problem. Furthermore, our earth is going to be an intolerable place to live providing we don’t find out a solution for it. It’s better to government focus their money on the people and earth problems first and then let space look after itself."""
}

data = {
    "text": """The websites I refer to do not have a specific date of update, but some resources you can refer to are:

Wikipedia (Last updated on 2023-01-30)
Philosophy Now (Last updated on 2021)
Stanford Encyclopedia of Philosophy (Last updated on 2022)
Intellectual Enlightenment refers to the development of reason, rationality, and critical thinking. It's the process of acquiring knowledge and understanding through the use of reason and logic.

Spiritual Enlightenment refers to a state of being where one experiences a deep sense of inner peace, interconnectedness with the universe, and an understanding of the true nature of reality. It often involves a spiritual awakening and a transformation of consciousness.

In short, Intellectual Enlightenment is about the growth of knowledge and understanding, while Spiritual Enlightenment is about the growth of the self and the inner experience.
"""
}


if __name__ == "__main__":
    is_debug = True

    print('This is CheckGPT - A neural network to detect content generated using big LMs (like ChatGPT, GPT3, GPT2)')
    print('For AI generated content detection, we are using statistical and heuristical methods, perplexity, entropy, '
          'coherence and consistency and other. Accuracy is up to 98%. Use our web app and RestAPI at checkgpt.app.')

    jsoned_req = json.dumps(data)
    if is_debug: print(jsoned_req)

    try:
        r = requests.post(url, data=jsoned_req, headers={'Content-Type': 'application/json'})
        if is_debug: print(r.text)
        answer = json.loads(r.text)
        print("Request ID:", answer["request_id"])
        print("Result:", answer["result"])
        print("Human score:", answer["human_score"])
        print("ChatGPT score:", answer["ChatGPT_score"])
        print("Execution time:", answer["execution_time"])
    except:
        print("Some error while sending POST request. Please check your connection and try again!")

    print('Done.')
