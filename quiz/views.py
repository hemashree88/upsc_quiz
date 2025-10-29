from django.shortcuts import render
import requests, random

# HOME PAGE
def home(request):
    return render(request, 'quiz/home.html')

# CATEGORY PAGE
def category(request):
    return render(request, 'quiz/category.html')

# QUESTION COUNT PAGE
def question_count(request):
    category = request.GET.get('category', 'general')
    return render(request, 'quiz/question_count.html', {'category': category})

# QUIZ PAGE
def quiz_page(request):
    if request.method == "POST":
        # when user submits answers
        questions = eval(request.POST.get('questions_data'))
        score = 0
        results = []
        for i, q in enumerate(questions):
            selected = request.POST.get(f"q{i}")
            correct = q['correct']
            if selected == correct:
                score += 1
            results.append({
                'question': q['question'],
                'selected': selected,
                'correct': correct,
                'options': q['options']
            })
        return render(request, 'quiz/result.html', {'results': results, 'score': score, 'total': len(questions)})

    else:
        # when quiz is starting
        category = request.GET.get('category', 'general')
        count = int(request.GET.get('count', 5))

        # Fetch questions via API (can replace with UPSC API later)
        api_url = f"https://opentdb.com/api.php?amount={count}&type=multiple"
        data = requests.get(api_url).json()

        questions = []
        for q in data['results']:
            options = q['incorrect_answers'] + [q['correct_answer']]
            random.shuffle(options)
            questions.append({
                'question': q['question'],
                'options': options,
                'correct': q['correct_answer']
            })

        return render(request, 'quiz/quiz.html', {'questions': questions})
