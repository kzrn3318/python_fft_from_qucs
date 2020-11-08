import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def import_data(csv_path):
    df = pd.read_csv(csv_path)
    df["time"] = df['time;"r Vo.Vt";"i Vo.Vt"'].apply(lambda x : x.split(";")[0])
    df["score"] = df['time;"r Vo.Vt";"i Vo.Vt"'].apply(lambda x : x.split(";")[1])
    df["time"] = df['time'].apply(lambda x : float(x))
    df["score"] = df['score'].apply(lambda x : float(x))
    time = df["time"].values
    score = df["score"].values

    step = time[1] - time[0]
    return time , score , step

def exchenge_data(time,data):
    ex_data = np.fft.fft(data)
    return  ex_data

def plot_data(time,score,step,flag):
    fig = plt.figure()
    n = score.shape[0]
    score = np.abs(score/(n/2))
    freq = np.fft.fftfreq(n,d=step)
    
    f = freq[0:int(n/2)]
    s = score[0:int(n/2)]
    plt.plot(f[:80],s[:80])
    plt.xlabel("Freqency[Hz]")
    plt.ylabel("magnitude")

    if flag==0:
        print("="*60)
        print("saveing image")
        fig.savefig("img.png")
        
        plt.plot(f,s)
        plt.xlabel("Freqency[Hz]")
        plt.ylabel("magnitude")
        fig.savefig("img_2.png")

        print("saveing done")
    else:
        plt.show()

def main():
    args = sys.argv
    path = args[1]
    flag = int(args[2])

    #0.0001
    print("import csv now")
    time , score , step= import_data(path)
    print("import csv done")
    print("="*60)

    print("exchenge now")
    score = exchenge_data(time, score)
    print("exchenge done")
    print("="*60)
    
    plot_data(time,score,step,flag)

if __name__=="__main__":
    main()