text = '''The Music  of the Ainur There was Eru,  the One,  who  in Arda is  called Iluvatar; and he  made  first the  Ainur,  the Holy  Ones, that  were the offspring of his  thought,  and they  were with  him before  aught else was made.  And he spoke to  them,  propounding to them  themes  of  music;  and they  sang  before him,  and he was  glad. But for a long while  they  sang only each alone,  or but  few  together, while the  rest hearkened; for each comprehended  only  that part of me  mind of  Iluvatar  from which  he  came,  and in the  understanding  of their brethren  they  grew  but slowly.  Yet ever  as  they  listened  they  came to deeper  understanding,  and increased in unison  and harmony.
And  it came to  pass  that  Iluvatar called together  all the  Ainur  and  declared  to  them a mighty  theme,  unfolding to  them things  greater and  more wonderful  than he had yet revealed; and the  glory  of its  beginning and the splendour  of its end amazed the  Ainur,  so that they  bowed  before Iluvatar and  were  silent.
Then Iluvatar  said to  them: 'Of the  theme  that I  have  declared  to  you  make Great  Music.'''

code = []


count = 0

for i in text:
    if i == " ":
        count = count + 1
    elif i != " " and count != 0:
        code.append(count)
        count = 0


print(code)



