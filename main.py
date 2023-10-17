import random

bot_greeting_messages = ["Hi, I am Alexander bot, What programming language are you interested in learning about?\n•Java\n•Python\n•C++\n•JavaScript\n•C#",
                         "Hello, What programming language are you interested in learning about?\n\n•Java\n•Python\n•C++\n•JavaScript\n•C#"]

bot_programming_languages = {"java": "Java is widely used in mobile app development, particularly for Android, the most popular mobile operating system. It's also a key language in web development, where it's employed in web applications, often through frameworks like Spring." ,
                      "python": "Python is a versatile language with a multitude of applications. It's used for web development, thanks to frameworks like Django and Flask. Python is also the go-to language for data analysis and data science, where libraries like NumPy, pandas, and scikit-learn are instrumental. Additionally, Python's simplicity and readability make it excellent for scripting and task automation. In the realm of Artificial Intelligence (AI), Python is indispensable, playing a pivotal role in developing AI solutions, bots, and task automation systems.",
                      "c++": "C++ is a powerful programming language with diverse applications. It is used extensively in the development of system software, including operating systems and hardware drivers, known for its high performance. Additionally, C++ is a go-to choice for the gaming industry and intensive graphics software, playing a pivotal role in the development of video games and high-performance graphics applications.",
                      "javascript": "JavaScript is a versatile language with a dual role in web development. It is primarily used for creating interactive and dynamic client-side websites, offering enhanced user experiences. Additionally, JavaScript, in conjunction with Node.js, enables server-side web application development, expanding its utility in the development of full-stack web applications.",
                      "c#": "Desarrollo de Software de Sistemas: Utilizado para desarrollar sistemas operativos, controladores de hardware y software de alto rendimiento. Juegos y Gráficos: Ampliamente empleado en el desarrollo de videojuegos y software de gráficos intensivos." } 



while True:
    
        
    user_message = input("\nWrite a messages: ")
    
    if user_message.lower() == "hi" or user_message.lower() == "hello":
        
      
        print(f"\nBot message: {random.choices(bot_greeting_messages)[0]}")
    
    
    elif user_message.lower() == "java":
        
        print(f"\n{bot_programming_languages['java']}")
        print("\nwhat other programming languages do you want to know? If you don't know more, write 'exit'")
    
    elif user_message.lower() == "python":
        
        print(f"\n{bot_programming_languages['python']}")
        print("\nwhat other programming languages do you want to know? If you don't know more, write 'exit'")
        
    elif user_message.lower() == "javascript":
            
            print(f"\n{bot_programming_languages['javascript']}")
            print("\nwhat other programming languages do you want to know? If you don't know more, write 'exit'")
    
    elif user_message.lower() == "c++":
            
            print(f"\n{bot_programming_languages['c++']}")
            print("\nwhat other programming languages do you want to know? If you don't know more, write 'exit'")
    
    elif user_message.lower() == "c#":
            
            print(f"\n{bot_programming_languages['c#']}")
            print("\nwhat other programming languages do you want to know? If you don't know more, write 'exit'")
    
    elif user_message.lower() == "exit":
        
        print("\nOkay, see you")
        break
    
    else:
        
        print("\nI do not understand your message. Repeat again please")
        
        
        