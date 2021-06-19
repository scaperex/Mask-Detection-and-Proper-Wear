from LightingModel import LitModel
import pytorch_lightning as pl
from maskData import MaskDataModule
import config as cfg

pl.seed_everything(8318)
if __name__ == '__main__':

    model = LitModel()
    data_module = MaskDataModule(train_dir=cfg.train_dir, val_dir=cfg.val_dir,
                               batch_size=cfg.batch_size, num_workers=cfg.num_workers)

    trainer = pl.Trainer(max_epochs=cfg.max_epochs, gpus=1, num_sanity_val_steps=0)
                     # ,limit_train_batches=600, limit_val_batches=10) # TODO full train
    trainer.fit(model, datamodule=data_module)

