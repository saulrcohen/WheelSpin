from main import start_spin
from constants import min_max

if __name__ == '__main__':
    vip_level = 1
    time_until_free_spin_eligible = 0
    min_value, max_value = min_max[vip_level]
    things_won, total_value, time_until_free_spin_eligible = start_spin(vip_level,
                                                                        time_until_free_spin_eligible=time_until_free_spin_eligible)

    print(f'Congrats! You won {things_won}')




