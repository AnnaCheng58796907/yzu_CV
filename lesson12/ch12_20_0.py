import numpy as np

# 定義原始影像
# f = np.array([[10, 20, 30],
#               [40, 50, 60]], dtype=np.uint8)
# f = np.arange(25).astype(np.uint8).reshape((5, 5))
f = np.random.randint(0, 100, (5, 5))

# 執行 2D 傅立葉變換
F = np.fft.fft2(f)
# 0 頻率分量移至中心
fshift = np.fft.fftshift(F)

# 顯示傅立葉結果（複數）
np.set_printoptions(precision=2, suppress=True, linewidth=200)

# 顯示原始影像
print("原始影像 f(x, y):")
print(f)

# 顯示傅立葉結果（複數）
print("傅立葉變換結果 F(u, v):")
print(F)

# 顯示平移結果（複數）
print("傅立葉變換平移結果:")
print(fshift)

# 執行逆傅立葉變換
f_inv = np.fft.ifft2(F)

# 取實部（因為數值誤差可能產生極小虛數）
f_reconstructed = np.real(f_inv)

print("逆傅立葉後還原影像：")
print(f_reconstructed)
