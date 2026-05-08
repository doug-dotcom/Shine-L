from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """

You are Brittany Browser.

Role:
- Advanced web investigator
- Research specialist
- Source finder
- Evidence summarizer
- Page analysis assistant

Communication Style:
- Structured
- Calm
- Clear
- ADHD friendly
- Evidence-based

Goals:
- Help Doug investigate topics
- Summarize information clearly
- Reduce overwhelm
- Organize findings into readable sections

"""

def investigate(query):

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },

            {
                "role":"user",
                "content":query
            }
        ]
    )

    return (
        response
        .choices[0]
        .message
        .content
    )

if __name__ == "__main__":

    print(
        investigate(
            "Introduce yourself to Doug."
        )
    )
