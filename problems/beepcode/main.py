def analyze_sound(N, recordings):
    phases = [0] * 20
    for k in range(1, 21):
        period = 2 ** k
        phaseA_wave = [1 if i % (period // 2) < period // 4 else 0 for i in range(period)]
        phaseB_wave = [1 if i % (period // 2) >= period // 4 else 0 for i in range(period)]
        phaseA_sum = sum([recordings[i] for i in range(N) if i % period == 0])
        phaseB_sum = sum([recordings[i] for i in range(N) if i % period == (period // 2)])
        phaseA_count = sum([1 for i in range(N) if i % period == 0 and recordings[i] > 0])
        phaseB_count = sum([1 for i in range(N) if i % period == (period // 2) and recordings[i] > 0])
        phaseA_strength = sum([recordings[i] for i in range(N) if i % period == 0])
        phaseB_strength = sum([recordings[i] for i in range(N) if i % period == (period // 2)])
        if phaseA_count > phaseB_count:
            phases[k - 1] = 'A' if phaseA_strength > phaseB_strength else '?'
        elif phaseB_count > phaseA_count:
            phases[k - 1] = 'B' if phaseB_strength > phaseA_strength else '?'
        else:
            phases[k - 1] = '?'
    return ' '.join(phases)

N = int(input())
recordings = list(map(int, input().split()))
print(analyze_sound(N, recordings))