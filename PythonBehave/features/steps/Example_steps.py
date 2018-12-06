
#behave Login.feature --tags=smoke
from behave import given, when, then, step

class StepDef():
    @given('we have behave installed')
    def step_impl(self):
        pass
    
    @when('we implement {number:d} tests')
    def step_impl1(self, number):  # -- NOTE: number is converted into integer
        assert number > 1 or number == 0
        self.tests_count = number
    
    @then('behave will test them for us!')
    def step_impl2(self):
        assert self.failed is False
        assert self.tests_count >= 0
        
    @when('we implement numOf tests')
    def step_impl3(self):
        for row in self.table:
            print(row['num'])
            assert row['num']>1 or row['num']==0
            self.tests_count=row['num']
    
