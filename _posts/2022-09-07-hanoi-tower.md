---
layout: post
title: 하노이 타워
post-title: 하노이 타워
date: 2022-09-07 02:18:00 +0900
permalink: /blog/hanoi_tower.html
permalink_name: /blog/hanoi_tower
category: blog
description: 코딩 테스트 입문 문제 중 하나인 하노이 타워 알고리즘 입니다. 보통 재귀함수를 통해 구현합니다. 여기서는 다른 방법으로 자료구조 스택 을 활용하여 구현하는 방법을 설명합니다. 코드는 파이썬으로 작성되었습니다.
tags: [code_test, algorithm]

detail_image: /assets/images/thumb/algorithm.png
---

<style>
.cropped {
width: 90%;
height: 850px;
object-fit: cover;
object-position: 50% 40%;
}
</style>

&nbsp; 하노이 타워는 3 개의 기둥에서 맨 왼쪽 기둥의 N 개의 서로 다른 크기의 내림차순 정렬된 원반들을 규칙을 따라 맨 오른쪽으로 완벽하게 똑같이 옮기는데 발생하는 최소 횟수를 구하는 문제입니다. 규칙은 다음 두 가지를 만족해야합니다.

- 원반은 한 번에 하나씩만 옮길 수 있다.
- 작은 원반 위에 그보다 큰 원반을 옮길 수 없다.

&nbsp; 하지만 대부분의 출제에서 원반의 이동순서만 요구하기 때문에 '(N-1) 개의 원반을 중간 기둥에 옮긴다'는 점을 활용하여 대부분의 풀이가 재귀함수(점화식)로 되어 있습니다.

<br>

```python
def Hanoi(N, From, To):

    if (N):
        Via = 6 - (From + To)
        Hanoi(N - 1, From, Via)
        print(From, To)
        Hanoi(N - 1, Via, To)


def main():
    N = int(input())
    Hanoi(N, 1, 3)


if __name__ == "__main__":
    main()
```

<br>

&nbsp; 이는 받아들이는 사람에 따라 다르겠지만 저의 경우에는 풀이가 <u>직관적</u>이지 않다고 생각됩니다. 재귀함수를 사용했기 때문에 그 과정이 잘 떠오르지 않습니다.

&nbsp; 또 다른 문제점은 N(타워의 높이)이 커짐에 따라 함수의 호출이 기하급수적으로 늘어나 결국 <u>스택오버플로우</u>가 발생한다는 것입니다.

&nbsp; 이 두 가지 문제점을 해결하기 원반의 이동 순서에 따른 데이터의 흐름을 파악할 필요가 있습니다. 즉, 하노이 타워의 원반을 이동시키는 논리를 찾아야 합니다.

<br>

---

&nbsp; 하노이 타워는 항상 기둥의 마지막에 놓인 원반만을 제어할 수 있다는 점에서 스택을 활용할 수 있습니다. 그리고 발생하는 데이터의 흐름을 파악하기 위해 N의 범위가 [1, 3] 일 때 원반의 이동 순서를 나열 해봅시다.

<br>

<p><center>
  <img src="/assets/images/content/hanoi/0.png" width="90%">
  <br>

  <span>그림 1. N[1, 3]</span>
</center></p>

<br>

&nbsp; 아직 완벽한 과정을 설명하기 힘들지만 적어도 규칙 하나를 발견할 수 있습니다. N이 짝수일 때와 홀수일 때 원반이 옮겨져야 할 기둥의 순서가 다르다는 것입니다.

<br>

<p><center>
  <img src="/assets/images/content/hanoi/1.png" width="60%" style="height: 580px; object-fit: cover;">
  <br>

  <span>그림 2. Move Disk, when N = 3</span>
</center></p>

<br>

&nbsp; 조금 더 직관적인 규칙을 찾기 위해 N = 3 인 경우, 원반이 이동하는 위치를 시각화 했습니다. 재귀함수를 통해 구현하면 얻을 수 있는 답과 같을 것입니다. 그림 2를 보면 또 하나의 규칙을 더 찾을 수 있습니다.

<br>

<p><center>
  <img src="/assets/images/content/hanoi/2.png" width="60%" style="height: 580px; object-fit: cover;">
  <br>

  <span>그림 3. Not selectable as From, when N = 3</span>
</center></p>

<br>

&nbsp; 이미 이전 단계에서 원반이 옮겨진 기둥(To)은 다음 원반을 옮길 기둥(From)으로 선택될 수 없다는 것 입니다. 만약 그것이 가능하다면 최소 횟수로 원반을 옮기지 못하게 될 것입니다. 이번에는 N = 3 일 때 두 번째 원반 이동 과정(그림 1에서 N = 3, K = 2)을 통해 원반을 옮기는 규칙을 알아보겠습니다.

<br>

<p><center>
  <img src="/assets/images/content/hanoi/3.png" width="100%">
  <br>

  <span>그림 4. N = 3, K = 2 시뮬레이션 순서</span>
</center></p>

<br>

&nbsp; 이 상황에서 원반을 옮기는 경우의 수는 위와 같이 총 6개 입니다. 또한 순서는 Case 1~6 순서로 시뮬레이션 합니다. 즉, N 이 홀수인 경우 원반을 첫 번째 기둥으로 부터 왼쪽으로 옮깁니다.

&nbsp; Case 1(첫 번째 순서)에서는 '작은 원반 위에 그보다 큰 원반을 옮길 수 없다'는 규칙을 위반합니다. 하지만 Case 2 는 옮기려는 위치에 원반이 없기 때문에 가능합니다. 이렇게 원반을 옮길 수 있는 경우 원반을 옮기며 다음 과정으로 넘어갑니다(break). 그리고 만약 Case 3 처럼 원반을 옮길 기둥으로 선택이 불가능하면 다음 Case 로 넘어갑니다(continue).

&nbsp; 이 논리를 그대로 N = 3 일 때 여섯 번 째 이동 과정에 적용해보겠습니다.

<br>

<p><center>
  <img src="/assets/images/content/hanoi/4.png" width="100%">
  <br>

  <span>그림 5. N = 3, K = 6 시뮬레이션 순서</span>
</center></p>

<br>

&nbsp; Case 1~2 의 경우 기둥이 From 으로 선택 될 수 없기 때문에 다음 Case 로 넘어갑니다. Case 3~5 은 작은 원반 위에 큰 원반을 옮기기 불가능합니다. 마지막 Case 6 에서는 모든 규칙을 만족하게 되어 원반이 옮겨지게 되며 다음 과정으로 넘어갑니다.

<br>

<p><center>
  <img src="/assets/images/content/hanoi/5.png" width="100%" style="height: 500px; object-fit: cover;">
  <br>

  <span>그림 6. Not selectable as From, when N = 4</span>
</center></p>

<br>

&nbsp; N이 짝수인 경우는 순서가 다릅니다. N = 2 인 경우는 원반을 옮기는 과정에 대한 예시가 너무 적어 N = 4 인 경우의 순서를 가져왔습니다. 앞에서 처럼 N = 4 일 때 두 번째 이동 과정을 확인해보겠습니다.

<br>

<p><center>
  <img src="/assets/images/content/hanoi/6.png" width="100%">
  <br>

  <span>그림 7. N = 4, K = 2 시뮬레이션 순서</span>
</center></p>

<br>

&nbsp; N이 짝수인 경우 원반을 첫 번째 기둥으로 부터 오른쪽으로 옮깁니다.

&nbsp; 앞에서와 마찬가지로 Case 1(첫 번째 순서)에서는 '작은 원반 위에 그보다 큰 원반을 옮길 수 없다'는 규칙을 위반합니다. 하지만 Case 2 는 옮기려는 위치에 원반이 없기 때문에 가능합니다. 마찬가지로 Case 3 처럼 원반을 옮길 기둥으로 선택이 불가능하면 다음 Case 로 넘어갑니다.

<br>

<p><center>
  <img src="/assets/images/content/hanoi/7.png" width="100%">
  <br>

  <span>그림 8. N = 4, K = 6 시뮬레이션 순서</span>
</center></p>

<br>

&nbsp; 다음은 N = 4, K = 6 일 때 시뮬레이션 순서입니다. Case 1~2 의 경우 기둥이 From 으로 선택 될 수 없기 때문에 다음으로 넘어갑니다. Case 3~5 은 작은 원반 위에 큰 원반을 옮기기 불가능하며 결국 Case 6에서 규칙을 만족하여 원반이 옮겨지게 됩니다.

<br>

---

<br>

<p><center>
  <img src="/assets/images/content/hanoi/Screenshot from 2022-09-08 14-09-49.png" width="100%">
  <br>

  <span>그림 8. 구현 코드 N = 4 실행결과</span>
</center></p>

<br>

&nbsp; 이렇게 하노이 타워의 최소 이동 횟수에 대한 모든 규칙을 찾았습니다. 이제는 구현이 남아있습니다. 코드는 이 글을 읽고 실제 구현하시는 분들도 있을 것이기 때문에 가렸습니다. 모든 규칙을 구현하게 되면 물론 코드는 길어지지만 해석은 데이터의 흐름이 구현되어 있기 때문에 훨신 직관적이게 됩니다.

&nbsp; 첫 포스트부터 자료구조를 활용하니 이전 포스트에 자료구조에 관해 다룬 내용이 없어 굉장히 허전합니다. 또한 마침 확인해보니 시뮬레이션 순서를 순열을 통해 구현할 수 있습니다. 따라서 다음 포스트는 자료구조나 확률과 통계에서 경우의 수를 따질 때 활용하는 순열, 조합에 대해 다뤄야 할 것 같습니다.

&nbsp; 이것으로 하노이 타워에 관한 글을 마치겠습니다. 읽어주셔서 감사합니다.

<br>

<details markdown="1"><summary>구현 코드</summary>

```python
class Stack:

    def __init__(self, N):
        self.n = N
        self.top = 0
        self.buffer = [None] * self.n

    @staticmethod
    def Render(stack):
        print(stack.buffer, end=" ")

    @property
    def IsFull(self):
        return (self.top >= self.n)

    @property
    def IsEmpty(self):
        return (self.top <= 0)

    @property
    def Peek(self):
        return self.buffer[self.top - 1]

    def Push(self, data):
        self.buffer[self.top] = data
        self.top += 1

    def Pop(self):
        self.top -= 1
        data = self.buffer[self.top]
        self.buffer[self.top] = None
        return data


def Solution(n):

    def DataRender(count, hanoi_tower, From, To):
        print(count, end=" ")

        for pole in hanoi_tower:
            Stack.Render(pole)

        print(From, To)

    def Proceeding(hanoi_tower):
        return not hanoi_tower[2].IsFull

    # Initialization
    order = [[[0, 1], [0, 2], [1, 2], [1, 0], [2, 0], [2, 1]],
             [[0, 2], [0, 1], [2, 1], [2, 0], [1, 0], [1, 2]]]
    hanoi_tower = []
    last = 3
    count = 0

    for i in range(last):
        hanoi_tower.append(Stack(n))    # Create Pole 0, 1, 2

    for i in range(n):
        hanoi_tower[0].Push(n - i)      # Push all Disk in Pole 0

    print(count, end=" ")

    for pole in hanoi_tower:
        Stack.Render(pole)

    print()

    # Function
    while (Proceeding(hanoi_tower)):

        for From, To in order[n % 2]:
            flag = False

            if (From != last):

                if (not hanoi_tower[From].IsEmpty):

                    if (hanoi_tower[To].IsEmpty):
                        flag = True

                    elif (hanoi_tower[From].Peek < hanoi_tower[To].Peek):
                        flag = True

            if (flag):
                hanoi_tower[To].Push(hanoi_tower[From].Pop())
                count += 1
                last = To
                DataRender(count, hanoi_tower, From, To)
                break

def main():

    n = int(input())
    Solution(n)

if __name__ == "__main__":
    main()
```

</details>

<br>
