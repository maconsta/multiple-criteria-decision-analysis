# Multiple Criteria Decision Analysis

## Todo:

* Да се разгледа и тества Topsis Pairwise метода дали работи правилно.
* Да се добавят unit tests за AHP метода.
* Да се допълни weighted_sum unit test-a.


## Done 

* Добавен е методa AHP.
* Оправена е стойността, която връщат методите topsis и WSM.
* Добавен е метода Electre


## Return Values of All Methods

* Всички методи трябва да връщат една и съща стойност. В момента методите връщат подреден в нисходящ ред списък от речници, в които има ключове "name" и "score". Списъкът е подреден по ключа "score".
  * Пример: [{"name": "BMW", "score": 0.95}, {"name": "Audi", "score": 0.7}, {"name": "Mercedes", "score": 0.56}]

