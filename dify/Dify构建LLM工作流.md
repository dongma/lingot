# Dify构建LLM工作流
> Dify使用文档，https://docs.dify.ai/zh/use-dify/getting-started/introduction

## Dify云平台注册
想快速开箱即用的话，可以用`github`或`google`账号在`Dify`云平台上注册 https://dify.ai/zh, 可以享受`200`次免费调用`OpenAI`接口的`SandBox`计划。

## Dify搭建AI应用
`stability`为图像生成应用，https://dreamstudio.stability.ai，注册获取`license`，并在`Dify`的`Tools`上进行注册。

```
prompt: 根据用户的提示，使用工具 stability_text2image 绘画指定内容，写实风格
和Bot聊天：在阳光下，一只狸花猫，戴着眼镜，伸懒腰
```
<div>
    <img src="../media/stability/6218224198d9425e8e64111e1ae33c01.png" width="520"/>
</div>

```
和Bot聊天：生成的图片 没有伸懒腰，重新生成下。 内心OS，"重新生成后，猫也没有伸懒腰，感觉stability AI生成不准确"。
```
<div>
    <img src="../media/stability/c9a26c94304b464eac300dc3c5a24ff9.png" width="520"/>
</div>

```
和Bot聊天：小猫和小狗一块儿玩耍，内心OS, "这次生成的还行"。
```
<div>
    <img src="../media/stability/8900b22e2fa04eac87b81181fb07731a.png" width="520"/>
</div>