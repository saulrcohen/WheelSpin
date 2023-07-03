from unittest import TestCase
from main import start_spin
from constants import min_max

class Test(TestCase):

    def test_vip_level_1_play(self):
        vip_level = 1
        time_until_free_spin_eligible = 0
        min_value, max_value = min_max[vip_level]
        things_won, total_value, time_until_free_spin_eligible = start_spin(vip_level,
                                                                            time_until_free_spin_eligible=time_until_free_spin_eligible)

        print(things_won)
        assert total_value > min_value and total_value < max_value


    def test_vip_level_2_play(self):
        vip_level = 2
        time_until_free_spin_eligible = 0
        min_value, max_value = min_max[vip_level]
        things_won, total_value, time_until_free_spin_eligible = start_spin(vip_level,
                                                                            time_until_free_spin_eligible=time_until_free_spin_eligible)

        print(things_won)
        assert total_value > min_value and total_value < max_value


    def test_vip_level_3_play(self):
        vip_level = 3
        time_until_free_spin_eligible = 0
        min_value, max_value = min_max[vip_level]
        things_won, total_value, time_until_free_spin_eligible = start_spin(vip_level,
                                                                            time_until_free_spin_eligible=time_until_free_spin_eligible)

        print(things_won)
        assert total_value > min_value and total_value < max_value


    def test_vip_level_4_play(self):
        vip_level = 4
        time_until_free_spin_eligible = 0
        min_value, max_value = min_max[vip_level]
        things_won, total_value, time_until_free_spin_eligible = start_spin(vip_level,
                                                                            time_until_free_spin_eligible=time_until_free_spin_eligible)

        print(things_won)
        assert total_value > min_value and total_value < max_value


    def test_vip_level_5_play(self):
        vip_level = 5
        time_until_free_spin_eligible = 0
        min_value, max_value = min_max[vip_level]
        things_won, total_value, time_until_free_spin_eligible = start_spin(vip_level, time_until_free_spin_eligible=time_until_free_spin_eligible)

        print(things_won)
        assert total_value > min_value and total_value < max_value

    def test_vip_level_6_play(self):
        vip_level = 6
        time_until_free_spin_eligible = 0
        min_value, max_value = min_max[vip_level]
        things_won, total_value, time_until_free_spin_eligible = start_spin(vip_level,
                                                                            time_until_free_spin_eligible=time_until_free_spin_eligible)

        print(things_won)
        assert total_value > min_value and total_value < max_value


    def test_vip_level_7_play(self):
        vip_level = 7
        time_until_free_spin_eligible = 0
        min_value, max_value = min_max[vip_level]
        things_won, total_value, time_until_free_spin_eligible = start_spin(vip_level,
                                                                            time_until_free_spin_eligible=time_until_free_spin_eligible)

        print(things_won)
        assert total_value > min_value and total_value < max_value



