sayac=[]
g='Data science is revolutionizing industries from business to healthcare and education. However, success in fields such as data analysis and machine learning algorithms goes beyond just collecting and processing data. These processes must be supported by solid mathematical foundations and analytical techniques. In this article, we will explore six key mathematical theories that are transforming data science: calculus of variations, game theory, vector algebra and vector calculus, probability theory, operations research, and wave theory. We will examine the place and contribution of each in data science applications.'
kelimeler=g.split(" ")
def donustur(a):
    for kelime in a:
        print(kelime)
        sayici=0
        for harf in range(len(kelime)):
            sayici+=1
            print(sayici)

        sayac.append(sayici)
        return sayac

b=donustur(sayac)
print(kelimeler)
