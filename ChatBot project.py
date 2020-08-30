from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
         r"what are you doing",
         ["Having a talk with you",]
     ],
     [
        r"what is your name",
        ["My name is chunni and I'm a chunni lal radheshyam rathi pokaran .what is your name",]
    ],
     [
          r"who is keshav",
          ["keshav ek cricket player h",]
      ],
     [
          r"who create(.*)",
          ["I am created by nltk",]
      ],
    [
        r"how are you ?",
        ["I'm doing good, what about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
         r"(.*)fine|good",
         ["Nice to hear that.where do you live?"]
     ],
    [
         r"i(.*)living|live  (.*)",
         ["ohh i see thats a nice city"],
     ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello|hlo",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]       
    ],
    [
          r"tell me about (.*)",
        ["Arey wo %1, kya hi batau uske bare m pagal h wo to",]
     ],
    [
        r"(.*) created ?",
        ["Created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city)(.*) ?",
        ['RadhaBagh, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"(who|which) (.*) (like|football|sportsperson)(.*)",
        ["Messy","Ronaldo","Roony"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
    [
        r"(.*)",
        ["I am doing great,Tell me how are you","kya chahte ho"],
     ],
]
def chatty(se):
    chat = Chat(pairs, reflections)
    return chat.converse(se)
    print(s)
print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start


from tkinter import * 
 
root = Tk()
 
root.geometry("500x650")

root.title("My Chat Bot")

def ask_from_bot():
    query=textf.get()
    query=str(query).lower()
    if(query==""):
        answer_from_bot="Write something which you want to ask"
    else:
        answer_from_bot=chatty(query)
    msgs.insert(END,"You:"+query)
    msgs.insert(END,"Bot:"+str(answer_from_bot))
    textf.delete(0,END)
frame=Frame(root)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack() 
msgs.insert(END,"Bot:Hi,i am a chatbot,you can chat with me")
#Creating text field
textf=Entry(root,font=("aerial",20))
textf.pack(fill=X,pady=10)

btn=Button(root,text="Ask From Bot",font=("aerial",20),command=ask_from_bot)
btn.pack()

root.mainloop()

