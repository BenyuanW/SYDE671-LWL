# Swin Transformer Reproducibility

We used the code provided in the original paper Swin Transformer to reproduce the image classification of the three variants in the original paper and added hyperparameter comparison experiments, ablation experiments, and self-attention module improvement experiments.

Among them, the hyperparameter comparison experiment includes learning rate comparison and batch size comparison, mainly to modify the config.py provided by the original author. 

For the ablation experiments, we remove the position embedding module, shifted window module, residual architecture, and dropout module, to testify the importance of each component.

For the improvement of the self-attention module, we reproduce four self-attention variants (Non-Local, A-SCN, Point-Attention, Offset-Attention), which are different from the self-attention module used in the original Swin Transformer.

By replacing the original self-attention module with the Non-Local variant which is one of the four variants above, we have improved the classification performance of the Swin transformer.

Additionally, we also used the Point-Attention variant to improve the training efficiency of the network, with similar accuracy.
