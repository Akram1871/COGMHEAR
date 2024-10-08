import numpy as np
import torch
from config import SEED
# fix random seeds for reproducibility
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = False
torch.backends.cudnn.benchmark = True
np.random.seed(SEED)

from argparse import ArgumentParser
from pytorch_lightning import Trainer
from pytorch_lightning.callbacks import ModelCheckpoint

from dataset import AVSEDataModule
from model import AVSEModule

def main(args):
    checkpoint_callback = ModelCheckpoint(monitor="val_loss_epoch")
    datamodule = AVSEDataModule(batch_size=args.batch_size)
    model = AVSEModule(val_dataset=datamodule.dev_dataset, lr=args.lr)
    trainer = Trainer.from_argparse_args(args, default_root_dir=args.log_dir, callbacks=[checkpoint_callback],
                                         accelerator="gpu", devices=1, max_epochs=args.max_epoch)
    trainer.fit(model, datamodule)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--batch_size", type=int, default=16, help="Batch size for training")
    parser.add_argument("--lr", type=float, default=0.0003, help="Learning rate for training")
    parser.add_argument("--log_dir", type=str, required=True, help="Path to save tensorboard logs")
    parser.add_argument("--max_epoch", type=int, default=20, help="Maximum Epochs number")
    parser = Trainer.add_argparse_args(parser)
    args = parser.parse_args()
    main(args)
