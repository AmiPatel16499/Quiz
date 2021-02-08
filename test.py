from User import Examiner,Candidate

e1=Examiner("E",234)
print(e1)
e1.addQuestion("maths","easy")
e1.addQuestion("maths","easy")
e1.addQuestion("maths","medium")
e1.displayAllQuestions()

c1=Candidate("S",2)
print(c1)
c1.viewTopics()
c1.run_test()
