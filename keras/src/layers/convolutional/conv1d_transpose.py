from keras.src.api_export import keras_export
from keras.src.layers.convolutional.base_conv_transpose import BaseConvTranspose


@keras_export(
    [
        "keras.layers.Conv1DTranspose",
        "keras.layers.Convolution1DTranspose",
    ]
)
class Conv1DTranspose(BaseConvTranspose):
    """1D transposed convolution layer.

    The need for transposed convolutions generally arise from the desire to use
    a transformation going in the opposite direction of a normal convolution,
    i.e., from something that has the shape of the output of some convolution
    to something that has the shape of its input while maintaining a
    connectivity pattern that is compatible with said convolution.

    Args:
        filters: int, the dimension of the output space (the number of filters
            in the transpose convolution).
        kernel_size: int or tuple/list of 1 integer, specifying the size of the
            transposed convolution window.
        strides: int or tuple/list of 1 integer, specifying the stride length
            of the transposed convolution. `strides > 1` is incompatible with
            `dilation_rate > 1`.
        padding: string, either `"valid"` or `"same"` (case-insensitive).
            `"valid"` means no padding. `"same"` results in padding evenly to
            the left/right or up/down of the input such that output has the same
            height/width dimension as the input.
        output_padding: An integer tuple/list of 1 integer specifying the
            amount of padding along the time dimension of the output tensor.
            The amount of output padding must be lower than the stride.
            If set to `None` (default), the output shape is inferred.
        data_format: string, either `"channels_last"` or `"channels_first"`.
            The ordering of the dimensions in the inputs. `"channels_last"`
            corresponds to inputs with shape `(batch, steps, features)`
            while `"channels_first"` corresponds to inputs with shape
            `(batch, features, steps)`. It defaults to the `image_data_format`
            value found in your Keras config file at `~/.keras/keras.json`.
            If you never set it, then it will be `"channels_last"`.
        dilation_rate: An integer tuple/list of 1 integer, specifying
            the dilation rate to use for dilated convolution.
            Currently, specifying a `dilation_rate` value != 1 is
            incompatible with specifying a stride value != 1.
            Also dilation rate larger than 1 is not currently supported.
        activation: Activation function. If `None`, no activation is applied.
        use_bias: bool, if `True`, bias will be added to the output.
        kernel_initializer: Initializer for the convolution kernel. If `None`,
            the default initializer (`"glorot_uniform"`) will be used.
        bias_initializer: Initializer for the bias vector. If `None`, the
            default initializer (`"zeros"`) will be used.
        kernel_regularizer: Optional regularizer for the convolution kernel.
        bias_regularizer: Optional regularizer for the bias vector.
        activity_regularizer: Optional regularizer function for the output.
        kernel_constraint: Optional projection function to be applied to the
            kernel after being updated by an `Optimizer` (e.g. used to implement
            norm constraints or value constraints for layer weights). The
            function must take as input the unprojected variable and must return
            the projected variable (which must have the same shape). Constraints
            are not safe to use when doing asynchronous distributed training.
        bias_constraint: Optional projection function to be applied to the
            bias after being updated by an `Optimizer`.

    Input shape:

    - If `data_format="channels_last"`:
        A 3D tensor with shape: `(batch_shape, steps, channels)`
    - If `data_format="channels_first"`:
        A 3D tensor with shape: `(batch_shape, channels, steps)`

    Output shape:

    - If `data_format="channels_last"`:
        A 3D tensor with shape: `(batch_shape, new_steps, filters)`
    - If `data_format="channels_first"`:
        A 3D tensor with shape: `(batch_shape, filters, new_steps)`

    Returns:
        A 3D tensor representing
        `activation(conv1d_transpose(inputs, kernel) + bias)`.

    Raises:
        ValueError: when both `strides > 1` and `dilation_rate > 1`.

    References:
    - [A guide to convolution arithmetic for deep learning](
        https://arxiv.org/abs/1603.07285v1)
    - [Deconvolutional Networks](
        https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf)

    Example:

    >>> x = np.random.rand(4, 10, 128)
    >>> y = keras.layers.Conv1DTranspose(32, 3, 2, activation='relu')(x)
    >>> print(y.shape)
    (4, 21, 32)
    """

    def __init__(
        self,
        filters,
        kernel_size,
        strides=1,
        padding="valid",
        output_padding=None,
        data_format=None,
        dilation_rate=1,
        activation=None,
        use_bias=True,
        kernel_initializer="glorot_uniform",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        **kwargs,
    ):
        super().__init__(
            rank=1,
            filters=filters,
            kernel_size=kernel_size,
            strides=strides,
            padding=padding,
            output_padding=output_padding,
            data_format=data_format,
            dilation_rate=dilation_rate,
            activation=activation,
            use_bias=use_bias,
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer,
            kernel_regularizer=kernel_regularizer,
            bias_regularizer=bias_regularizer,
            activity_regularizer=activity_regularizer,
            kernel_constraint=kernel_constraint,
            bias_constraint=bias_constraint,
            **kwargs,
        )
