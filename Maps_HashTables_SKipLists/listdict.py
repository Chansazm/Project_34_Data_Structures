# eng_di = {}
# eng_di['solitude'] =['lone','lonely','alone','unaccompanied','without someone']
# eng_di['hope'] = ['aspiration','desire','wish','expectation','ambition']
# print(eng_di)



eng_di = {'solitude':[]}
eng_words = ['lone','lonely','alone','unaccompanied','without someone']
eng_di['solitude'].append(eng_words[0])

eng_di['solitude'] = eng_words
# print(eng_di)

if (eng_di.get('solitude')):
    for listitem in eng_di['solitude']:
        print(listitem)
else:
    print("word not found")