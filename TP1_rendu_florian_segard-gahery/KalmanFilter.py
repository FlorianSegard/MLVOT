import numpy as np

class KalmanFilter:
    def __init__(self, dt, u_x, u_y, std_acc, x_sdt_meas, y_sdt_meas):
        self.u = np.array([[u_x, u_y]]).T
        self.x_k = np.array([[0, 0, 0, 0]]).T
        self.A = np.array([[1, 0, dt, 0], 
                           [0, 1, 0, dt], 
                           [0, 0, 1, 0], 
                           [0, 0, 0, 1]])
        self.B = np.array([[0.5 * (dt ** 2), 0], 
                           [0, 0.5 * (dt ** 2)], 
                           [dt, 0], 
                           [0, dt]])
        self.H = np.array([[1, 0, 0, 0], 
                           [0, 1, 0, 0]])
        self.Q = std_acc * np.array([[0.25 * (dt ** 4), 0, 0.5 * (dt ** 3), 0], 
                                     [0, 0.25 * (dt ** 4), 0, 0.5 * (dt ** 3)],
                                     [0.5 * (dt ** 3), 0, dt ** 2, 0],
                                     [0, 0.5 * (dt ** 3), 0, dt ** 2]])
        self.R = np.array([[x_sdt_meas ** 2, 0],
                           [0, y_sdt_meas ** 2]])
        self.P = np.array([[1, 0, 0, 0], 
                           [0, 1, 0, 0], 
                           [0, 0, 1, 0], 
                           [0, 0, 0, 1]])
    
    def predict(self):
        self.x_k = self.A @ self.x_k + self.B @ self.u
        self.P = self.A @ self.P @ self.A.T + self.Q
        return self.x_k, self.P
        
    def update(self, z_k):
        S_k = self.H @ self.P @ self.H.T + self.R
        K_k = self.P @ self.H.T @ np.linalg.inv(S_k)
        self.x_k = self.x_k + K_k @ (z_k - self.H @ self.x_k)
        self.P = (np.eye(4) - K_k @ self.H) @ self.P
