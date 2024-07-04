def algoritmo_LMS(X, yd, alfa, epochs):
    import numpy as np
    import matplotlib.pyplot as plt

    w = np.random.rand(X[0].size)  # w = np.array([0.5, -0.25, 0.75])
    #w = np.array([0.62, 0.75, -0.35])
    error = np.array([])
    k = np.array([])
    j = 0

    for epoca in range(epochs):

        for i, x in enumerate(X):
            v = np.dot(w, x)
            print('salida v =', v)

            y = sgn(v)
            print('salida y =', y)

            e = yd[i] - y
            print('error =', e)

            w = w + alfa * e * x / (np.linalg.norm(x) ** 2)
            print('vector de pesos =', w)

            error = np.append(error, e)
            k = np.append(k, j)
            j += 1

    print('iteraciones: ', k)
    # print error

    plt.plot(k, error)
    plt.xlabel('iteracion k')
    plt.ylabel('error')
    plt.show()

    return w


def percep_out(input_pat, w):
    import numpy as np

    output_class = np.array([])

    for i, x in enumerate(input_pat):
        v = np.dot(w, x)
        y = sgn(v)
        output_class = np.append(output_class, y)

    return output_class


def bound_reg(X, t, w):
    import numpy as np
    import matplotlib.pyplot as plt

    x_min, x_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    y_min, y_max = X[:, 2].min() - 0.5, X[:, 2].max() + 0.5

    xx = np.linspace(x_min, x_max)
    yy = -(w[1] / w[2]) * xx - (w[0] / w[2])

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xlabel('Caracteristica x1')
    plt.ylabel('Caracteristica x2')
    plt.title('Clasificador lineal')
    plt.plot(xx, yy, 'g-')
    plt.scatter(X[:, 1], X[:, 2], s=200, alpha=0.7, cmap=plt.cm.coolwarm, c=t)
    plt.show()


def patrones_graph(X, t):
    import numpy as np
    import matplotlib.pyplot as plt

    ###fig, ax = plt.subplots()  ####

    x_min, x_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    y_min, y_max = X[:, 2].min() - 0.5, X[:, 2].max() + 0.5

    classes = [-1, 1]
    # xx = np.linspace(x_min, x_max)
    # yy = -(w[1]/w[2])*xx -(w[0]/w[2])
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xlabel('Caracteristica x1')
    plt.ylabel('Caracteristica x2')
    plt.title('Patrones')
    ##plt.grid(True)  ####
    ##plt.legend()   ####
    # plt.plot(xx, yy, 'g-')
    # fig, ax = plt.subplots()
    plt.scatter(X[:, 1], X[:, 2], s=200, alpha=0.7, cmap=plt.cm.coolwarm, c=t)
    # plt.scatter(X[:, 1], X[:, 2], s= 200, alpha=0.7, cmap=plt.cm.coolwarm, c = t)
    # ax.legend(loc='upper left', frameon=False)
    # fig

    plt.show()  ####
    ###fig


def patrones_graph_legend(X, t):  ## solo para wine dataset caso muy particular

    import numpy as np
    import matplotlib.pyplot as plt

    plt.scatter(X[0:59, 1], X[0:59, 2], s=200, alpha=0.6, color='goldenrod', label='clase 0')
    plt.scatter(X[59:108, 1], X[59:108, 2], s=200, alpha=0.6, color='darkviolet', label='clase 1')
    plt.xlabel('Grado de alcohol')
    plt.ylabel('Melic acid')
    plt.title('Clases de vino')
    plt.legend(loc='upper left')
    plt.show()


def sgn(v):
    if v < 0:
        return -1.0
    else:
        return 1.0
import numpy as np
import matplotlib.pyplot as plt

x=np.array([[1.0,4.0,-1.5],
            [1.0,-2.0,-2.0],
            [1.0,2.75,1.5],
            [1.0,-0.5,1.0],
            [1.0,1.0,2.5],
            [1.0,2.0,1.2]])

y=np.array([1,1,-1,1,-1,-1])

#algoritmo_LMS(x,y,0.2,20)
patrones_graph(x,y)
