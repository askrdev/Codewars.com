""" 
Codewars.com/Cat years, Dog years| 8 Kyu  
"""

"""
Task
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year | 24 years
+4 cat years for each year after that | third years is 28 
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
"""

"""
Example input
def fixed_tests():
    @test.it("one")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(1), [1,15,15])
    @test.it("two")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(2), [2,24,24])
    @test.it("ten")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(10), [10,56,64])
"""

human_years = 3

def human_years_cat_years_dog_years(human_years):
    # Your code here
    return [human_years,human_years *15,human_years * 15] if human_years == 1 else [human_years,15+9,15+9] if human_years == 2 else [human_years, 4*human_years +16 , 5 * human_years + 14]

print(human_years_cat_years_dog_years(human_years))

# *** Jawaban Simple ***
# hy = 3
# def human_years_cat_years_dog_years(hy):
#     return [hy, 16 + 4 * hy, 14 + 5 * hy] if hy > 1 else [1,15,15]

# print(human_years_cat_years_dog_years(hy))
