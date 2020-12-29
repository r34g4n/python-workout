def run_timing():
    total_time = 0.0
    number_of_runs = 0
    while True:
        run_time = input('Enter 10km run time: ')
        if run_time == '':
            break
        try:
            run_time = float(run_time)
            number_of_runs += 1
            total_time += run_time
        except ValueError:
            print('Ignoring input...')
    avg = total_time / number_of_runs
    print(f'Average of {avg:.2f}, over {number_of_runs} runs')
    return avg, number_of_runs


run_timing()
