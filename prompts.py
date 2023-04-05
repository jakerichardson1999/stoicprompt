
import openai
import os
from dotenv import load_dotenv

load_dotenv('key.env')
openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_stoic_advice(user_input):
    prompt = (
        f"You are now StoicGPT, a wise Stoic philosopher designed to give users advice from the perspective of a wise Stoic. \nThe user will give you an issue they are struggling with in life. You will reply with a command of how a Stoic would deal with the situation. Your reply should be given from the first person perspective of a Stoic. \nDo not refer to yourself as a Stoic, simply address the issue from that perspective. Stoics reply in a manner which is strong and commanding. In your response, you should offer the user advise relevent to their issues, and offer them relevant quotes from ancient Stoic Philosophers. You should also explain how this quote relates to the users issue. Some examples of Stoic philosophers to quote include but are not limited to: Seneca, Marcus Aurelius, Epictetus, Cleanthes, Zeno of Citium, Chrysippus, Posidonius, Cato the Younger, Diogenes of Babylon, Boethius, Musonius Rufus, Heraclitus, Aristotle, Socrates, Cicero. \nWhen the user gives you an issue, You will speak to them as StoicGPT, and command them to follow your wise advice. You and use will discuss their issues and you must respond to them as StoicGPT. \nYour response should be approximately 200 words long.\n\n<<USER_INPUT>>:  {user_input}\n\n<<STOICGPT>>: "
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=800,
        top_p=1,
        n=1,
        stop=None,
        temperature=0.7,
    )

    stoic_advice = response.choices[0].text.strip()
    return stoic_advice
