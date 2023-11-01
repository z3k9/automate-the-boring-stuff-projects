import pyinputplus as pyip
import random, time

num_of_questions = 10
correct_ans = 0

for quest_num in range(num_of_questions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s * %s = '% (quest_num, num1, num2)

    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Took too long to answer')
    except pyip.RetryLimitException:
        print('Tried too many times')
    else:
        print('Correct !')
        correct_ans += 1
    time.sleep(2)

print('Score: %s / %s ' % (correct_ans, num_of_questions))