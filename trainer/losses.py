import torch.nn as nn

class ConfigurableLoss(nn.Module):
    def __init__(self, opt, env):
        super(ConfigurableLoss, self).__init__()
        self.opt = opt
        self.env = env
        self.metrics = []

    # net is either a scalar network being trained or a list of networks being trained, depending on the configuration.
    def forward(self, net, state):
        raise NotImplementedError

    def is_stateful(self) -> bool:
        """
        Losses can inject into the state too. useful for when a loss computation can be used by another loss.
        if this is true, the forward pass must return (loss, new_state). If false (the default), forward() only returns
        the loss value.
        """
        return False

    def extra_metrics(self):
        return self.metrics

    def clear_metrics(self):
        self.metrics = []

