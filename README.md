## human-computing-experiment

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)  
휴먼컴퓨팅 인터페이스 실험 관련 코드입니다.
실험은 음성 ai의 목소리에 따라서 사용자가 미치는 영향이 어떤지 분석하기 위해 프로그램을 작성하였습니다.
본 프로그램은 음성 ai의 어투등에 따라 사용자가 친근감을 느끼는지 도움을 주는지 조사를 하였습니다.

## Requirements

프로그램을 실행하기 위해 필요한 `requirements.txt`파일을 작성하였습니다.
라이브러리를 설치할라면 다음과 같이 입력하세요

```sh
$ pip install -r requirements.txt
```

## Project Organization
```
├── LICENSE
├── README.md
└── src <- Source code for use in this project
   │
   ├── mic <- mic 인식 코드 작성
   │   └── microphone_stream.py
   │ 
   ├── speaker_err.py   <- 기존 음성 스피커
   │ 
   ├── speaker_hel.py   <- 실질적인 도움을 말하는 음성 스피커
   │ 
   ├── speaker_umo.py   <- 과장되지 않은 유머를 말하는 음성 스피커
   │
   └── speaker_hum.py   <- 겸손한 태도로 말하는 음성 스피커
```

## Experiments
1. 실험은 총 4번에 걸쳐서 진행했습니다.
2. 각 피험자의 스피커 순서를 바꾸면서 실험을 진행했습니다.
3. 스피커 한번을 들려주고 그에 따른 설문조사를 진행하였습니다.
