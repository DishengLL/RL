import gym # 导入Gym 的Python 接口环境包
env = gym.make('CartPole-v1') # 构建实验环境
env.reset() # 重置一个回合
count = 0
for _ in range(100):
    count +=1
    env.render() # 显示图形界面
    action = env.action_space.sample() # 从动作空间中随机选取一个动作
    env.step(action)
    # x= env.step(action) # 用于提交动作，括号内是具体的动作
    # if x[2]==True:
    #
    # if count == 3:
    #     break

env.close() # 关闭环境