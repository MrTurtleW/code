import numpy as np

from .layer_utils import affine_relu_forward, affine_relu_backward,\
    affine_bn_relu_forward, affine_bn_relu_backward
from .layers import affine_forward, affine_backward, softmax_loss,\
    dropout_forward, dropout_backward

class TwoLayerNet:
    """
    A two-layer fully-connected neural network with ReLU nonlinearity and
    softmax loss that uses a modular layer design. We assume an input dimension
    of D, a hidden dimension of H, and perform classification over C classes.

    The architecture should be affine - relu - affine - softmax

    Note that this class does not implement gradient descent; instead, it will
    interact with a separate Solver object that is responsible for running optimization

    The learning parameters of the model are stored in the dictionary self.params that
    maps parameter names to numpy arrays.
    """
    def __init__(self, input_dim=3*32*32, hidden_dim=100, num_classes=10,
                       weight_scale=1e-3, reg=0.0):
        """
        Initialize a new network

        Inputs:
            - input_dim: An integer giving the size of the input
            - hidden_dim: An integer giving the size of the hidden layer
            - num_classes: An integer giving the number of classes to classify
            - dropout: Scalar between 0 and 1 giving dropout strength
            - weight-scale: Scalar giving the standard deviation for random
                initialization of the weights
            - reg: Scalar giving L2 regularization strength
        """
        self.params = {}
        self.reg = reg

        self.params['W1'] = weight_scale * np.random.randn(input_dim, hidden_dim)
        self.params['b1'] = np.zeros(hidden_dim)
        self.params['W2'] = weight_scale * np.random.randn(hidden_dim, num_classes)
        self.params['b2'] = np.zeros(num_classes)

    def loss(self, X, y=None):
        """
        Compute the loss and gradient for a minibatch of data.

        Inputs:
            - X: Array of input data of shape (N, d1, ..., d_k)
            - y: Array of labels, of shape (N,) y[i] gives the label of X[i]

        Returns:
            If y is None, then run a test-time forward pass for the model and return:
            - scores: Array of shape (N, C) giving classification scores, where scores[i, c]
                is the classification score for N[i] and class c
            If y is not None, then run a training-time forward and backward pass and return
            a tuple of
            - loss: Scalar value giving the loss
            - grads: Dictionary with the same keys as self.params, mapping parameter names 
                to gradients of the loss with respect to those parameters.
        """
        ar1_out, ar1_cache = affine_relu_forward(X, self.params['W1'], self.params['b1'])
        a2_out, a2_cache = affine_forward(ar1_out, self.params['W2'], self.params['b2'])
        scores = a2_out

        if y is None:
            return scores

        grads = {}
        loss, dscores = softmax_loss(scores, y)
        loss = loss + 0.5 * self.reg * np.sum(self.params['W1'] * self.params['W1']) + 0.5 * self.reg * np.sum(self.params['W2'] * self.params['W2'])
        dx2, dw2, db2 = affine_backward(dscores, a2_cache)
        grads['W2'] = dw2 + self.reg * self.params['W2']
        grads['b2'] = db2

        dx1, dw1, db1 = affine_relu_backward(dx2, ar1_cache)
        grads['W1'] = dw1 + self.reg * self.params['W1']
        grads['b1'] = db1

        return loss, grads

class FullyConnectedNet:
    """
    A fully-connected neural network with an arbitrary number of hidden layers, ReLU
    nonlinearities, and a softmax loss function. This will also implement dropout 
    and batch normalization as options. for a network with L layers, the architecture
    will be

    (affine - [batch_norm] - relu - [dropout]) x (L - 1) - affine - softmax
    """

    def __init__(self, hidden_dims, input_dim=3*32*32, num_classes=10,
                 dropout=0, use_batchnorm=False, reg=0.0,
                 weight_scale=1e-2, dtype=np.float32, seed=None):
        """
        Initialize a new FullyConnectedNet

        Inputs:
            - hidden_dims: A list of integers giving the size of each hidden layer.
            - input_dim: An integer giving the size of the input
            - num_classes: An integer giving the number of classes to classify.
            - dropout: Scalar between 0 and 1 giving dropout strength. If dropout=0 then
                the network should not use dropout at all.
            - use_batchnorm: Whether or not the network should use batch normalization.
            - reg: Scakar giving L2 regularization strength.
            - weight_scale: Scalar giving the standard deviation for random initialization
                of the weights
            - dtype: A numpy datatype object; all computions will be performed using this
                datatype. float32 is faster but less accurate, so you shold use float64
                for numeric gradient checking
            - seed: If not None, then pass this random seed to the dropout layers. This will
                make the dropout layers deteriminstic so we can gradient check the model.
        """
        self.use_batchnorm = use_batchnorm
        self.use_dropout = dropout > 0
        self.reg = reg
        self.num_layers = 1 + len(hidden_dims)
        self.dtype = dtype
        self.params = {}

        layer_input_dim = input_dim
        for i, hd in enumerate(hidden_dims):
            self.params['W{}'.format(i+1)] = weight_scale * np.random.randn(layer_input_dim, hd)
            self.params['b{}'.format(i+1)] = weight_scale * np.zeros(hd)

            if self.use_batchnorm:
                self.params['gamma{}'.format(i+1)] = np.ones(hd)
                self.params['beta{}'.format(i+1)] = np.zeros(hd)

            layer_input_dim = hd
        self.params['W{}'.format(self.num_layers)] = weight_scale * np.random.randn(layer_input_dim, num_classes)
        self.params['b{}'.format(self.num_layers)] = weight_scale * np.zeros(num_classes)

        # When using dropout we need to pass a dropout_param dictionary to each
        # dropout layer so that the layer knows the dropout probability and the mode
        # (train /test). You can pass the same dropout_param to each dropout layer.
        self.dropout_param = {}
        if self.use_dropout:
            self.dropout_param = {'mode': 'train', 'p': dropout}
            if seed is not None:
                self.dropout_param['seed'] = seed

        # With batch normalization we need to keep track of running means and
        # variances, so we need to pass a special bn_param object to each batch
        # normalization layer. You should pass self.bn_params[0] to the forward pass
        # of the first batch normalization layer, self.bn_params[1] to the forward
        # pass of the second batch normalization layer, etc.
        self.bn_params = []
        if self.use_batchnorm:
            self.bn_params = [{'mode': 'train'} for i in range(self.num_layers - 1)]

        # Cast all parameters to the correct datatype
        for k, v in self.params.items():
            self.params[k] = v.astype(dtype)

    def loss(self, X, y=None):
        """
        Compute loss and gradient for the fully-connected net

        Input / output: Same as TwolayerNet above.
        """
        X = X.astype(self.dtype)
        mode = 'test' if y is None else 'train'

        # Set train / test mode for batchnorm params and dropout param since they
        # behave differently during training and testing
        if self.dropout_param is not None:
            self.dropout_param['mode'] = mode
        if self.use_batchnorm:
            for bn_param in self.bn_params:
                bn_param['mode'] = mode


        ###########################################################################################
        # The forward pass for the fully-conntected net
        layer_input = X
        ar_cache = {}
        dp_cache = {}
        
        for lay in range(self.num_layers - 1):
            if self.use_batchnorm:
                layer_input, ar_cache[lay] = affine_bn_relu_forward(layer_input,
                                                                    self.params['W{}'.format(lay+1)],
                                                                    self.params['b{}'.format(lay+1)],
                                                                    self.params['gamma{}'.format(lay+1)],
                                                                    self.params['beta{}'.format(lay+1)],
                                                                    self.bn_params[lay])
            else:
                layer_input, ar_cache[lay] = affine_relu_forward(layer_input,
                                                                 self.params['W{}'.format(lay+1)],
                                                                 self.params['b{}'.format(lay+1)])

            if self.use_dropout:
                layer_input, dp_cache[lay] = dropout_forward(layer_input, self.dropout_param)

        ar_out, ar_cache[self.num_layers] = affine_forward(layer_input,
                                                           self.params['W{}'.format(self.num_layers)],
                                                           self.params['b{}'.format(self.num_layers)])
        scores = ar_out

        ###########################################################################################

        if mode == 'test':
            return scores

        ###########################################################################################
        # backward pass for the fully-connected net.
        loss, grads = 0.0, {}
        param_name = 'W{}'.format(self.num_layers)

        loss, dscores = softmax_loss(scores, y)
        dhout = dscores
        loss = loss + 0.5 * self.reg * np.sum(self.params[param_name]**2)
        dx, dw, db = affine_backward(dhout, ar_cache[self.num_layers])
        grads[param_name] = dw + self.reg * self.params[param_name]
        grads['b{}'.format(self.num_layers)] = db

        dhout = dx

        for idx in range(self.num_layers - 1):
            lay = self.num_layers - 1 - idx -1
            loss = loss + 0.5 * self.reg * np.sum(self.params['W{}'.format(lay+1)]**2)
            if self.use_dropout:
                dhout = dropout_backward(dhout, dp_cache[lay])
            if self.use_batchnorm:
                dx, dw, db, dgamma, dbeta = affine_bn_relu_backward(dhout, ar_cache[lay])
            else:
                dx, dw, db = affine_relu_backward(dhout, ar_cache[lay])
            grads['W{}'.format(lay+1)] = dw + self.reg * self.params['W{}'.format(lay+1)]
            grads['b{}'.format(lay+1)] = db
            if self.use_batchnorm:
                grads['gamma{}'.format(lay+1)] = dgamma
                grads['beta{}'.format(lay+1)] = dbeta

            dhout = dx
        ###########################################################################################
        return loss, grads