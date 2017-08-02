import core

def test_cost_of_tents():
    assert core.cost_of_tents('1') == 50

def test_cost_of_tents2():
    assert core.cost_of_tents('2') == 75

def test_cost_of_tents3():
    assert core.cost_of_tents('3') == 82

def test_cost_of_tents4():
    assert core.cost_of_tents('4') == 115

def test_cost_of_tents5():
    assert core.cost_of_tents('5') == 170

def test_cost_of_tents6():
    assert core.cost_of_tents('6') == 285

def test_cost_of_tents7():
    assert core.cost_of_tents('7') == 75

def test_cost_of_tents8():
    assert core.cost_of_tents('8') == 125

def test_cost_of_tents9():
    assert core.cost_of_tents('9') == 132

def test_cost_of_tents10():
    assert core.cost_of_tents('10') == 165

def test_cost_of_tents11():
    assert core.cost_of_tents('11') == 220

def test_cost_of_tents12():
    assert core.cost_of_tents('12') == 335

def test_deposit():
    assert core.deposit('50') == 5.0

def test_deposit2():
    assert core.deposit('75') == 7.5

def test_total():
    assert core.total('50') == 3.5

def test_type_of_tents():
    assert core.type_of_tents() == ['Tent 1 = 10X10\t\t' 'Tent 7 = 10X10 w/ 6 chairs & 1 table',
    'Tent 2 = 10X20\t\t' 'Tent 8 = 10X20 w/ 15 chairs & 3 tables',
    'Tent 3 = 16X16\t\t' 'Tent 9 = 16X16 w/ 20 chairs & 4 tables',
    'Tent 4 = 20X20\t\t' 'Tent 10 = 20X20 w/ 40 chairs & 6 tables',
    'Tent 5 = 20X30\t\t' 'Tent 11 = 20X30 w/ 55 chairs & 7 tables',
    'Tent 6 = 20X40\t\t' 'Tent 12 = 20X40 w/ 70 chairs & 8 tables']

def test_actual_cost():
    assert core.actual_cost('1') == 150

def test_actual_cost2():
    assert core.actual_cost('2') == 225

def test_actual_cost3():
    assert core.actual_cost('3') == 246

def test_actual_cost4():
    assert core.actual_cost('4') == 345

def test_actual_cost5():
    assert core.actual_cost('5') == 510

def test_actual_cost6():
    assert core.actual_cost('6') == 855

def test_actual_cost7():
    assert core.actual_cost('7') == 225

def test_actual_cost8():
    assert core.actual_cost('8') == 375

def test_actual_cost9():
    assert core.actual_cost('9') == 396

def test_actual_cost10():
    assert core.actual_cost('10') == 495

def test_actual_cost11():
    assert core.actual_cost('11') == 660

def test_actual_cost12():
    assert core.actual_cost('12') == 1005
