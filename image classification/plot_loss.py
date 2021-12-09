import matplotlib.pyplot as plt
import torch
import numpy as np
def plot_loss():
    plt.figure(figsize=(10,8))
    y = []

    p_linewidth=0.5
    enc = torch.load('/content/drive/MyDrive/baseloss/epoch_299')
    tempy = list(enc)
    y += tempy
    x = range(0,len(y))
    plt.plot(x, y, '-', linewidth=p_linewidth,label="Swin-B")

    y = []

    enc = torch.load('/content/drive/MyDrive/picture/tinyloss_batch_size_64/epoch_299.zip')
    tempy = list(enc)
    y += tempy
    x = range(0,len(y))
    plt.plot(x, y, '-', linewidth=p_linewidth,label="Swin-T")

    y = []

    enc = torch.load('/content/drive/MyDrive/smallloss/epoch_299')
    tempy = list(enc)
    y += tempy
    x = range(0,len(y))
    plt.plot(x, y, '-', linewidth=p_linewidth,label="Swin-S")

  

    
    plt_title = 'Backbone'
    plt.title(plt_title)
    plt.xlabel('epoch')
    plt.ylabel('LOSS')
    print('dddd2')
    # plt.savefig("/content/drive/MyDrive/1.png")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_loss()
