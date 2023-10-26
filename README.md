# Multiple Criteria Decision Analysis

## Todo:

* Да се разгледа и тества Topsis Pairwise метода дали работи правилно.
* Да се реализира правилно AHP метода, като се ползва основата, която е в проекта.
* Да се допълни weighted_sum unit test-a.


## Done 

* Оправена е стойността, която връщат методите topsis и WSM.
* Добавен е метода Electre и unit tests към него.
* Добавен е метода SMART и unit tests към него.


## Return Values of All Methods

* Всички методи трябва да връщат една и съща стойност. В момента методите връщат подреден в нисходящ ред списък от речници, в които има ключове "name" и "score". Списъкът е подреден по ключа "score".
  * Пример: [{"name": "BMW", "score": 0.95}, {"name": "Audi", "score": 0.7}, {"name": "Mercedes", "score": 0.56}]

