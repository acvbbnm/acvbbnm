# 김병우

보안관제·침해사고 대응 · 디지털 포렌식

<p align="center"><a href="https://cooperative-cave-e9b.notion.site/41c70716154e81b289fde409f3bae4c9">Notion 포트폴리오</a> · <a href="https://github.com/acvbbnm?tab=repositories">GitHub 프로젝트</a></p>

---

## 프로젝트

### [SIEM 공격 탐지·대응 실습](https://github.com/acvbbnm/siem-project)

공격 경로와 탐지 사각지대를 대조한 가상 SOC · 개인 프로젝트

공격망·DMZ·내부망·관리망을 분리하고 Snort·WAF·서버 로그를 Splunk에서 분석했습니다. Snort 룰 9개를 구성했고, Splunk 경보 5종 중 4종에서 총 8건의 발생을 확인했습니다. SPL은 실행 확인 범위를 나눠 기록했습니다.

<sub>Splunk · Snort · ModSecurity · 탐지·미탐 분석 · 차단 후 재검증</sub>

[최종 보고서](https://github.com/acvbbnm/siem-project/blob/main/report/README.md) · [탐지 룰과 SPL](https://github.com/acvbbnm/siem-project/blob/main/detection/README.md)

### [Evidence Atlas](https://github.com/acvbbnm/dfir)

Windows 포렌식 조사 도구 · 개인 프로젝트

KAPE CSV 산출물의 원래 행·해시·시각 의미를 보존하고, 시간축과 공유 참조 그래프로 탐색하도록 만들었습니다. Sigma 탐지 후보·로컬 AI 가설과 manifest 기반 사건 가져오기를 연결했습니다.

<sub>Python · SQLite · Neo4j · Elasticsearch · Sigma · 근거 보존</sub>

[설계서](https://github.com/acvbbnm/dfir/blob/main/DESIGN.md). AWS 확장은 코드와 로컬 검증까지 마쳤고, 실제 AWS에는 아직 배포하지 않았습니다.

### [AI Sherpa](https://github.com/acvbbnm/cloud)

클라우드 사고조사 가이드 · 정보보호 캡스톤, 4인 팀 팀장

설문에서 조사 초기에 어떤 로그부터 확인할지 정하기 어렵다는 점을 확인했습니다. 팀장을 맡아 사고 추적 엔진, 수집 가이드, 로그 정규화와 화면 연동을 구현했습니다.

<sub>조사 설계 · 베이즈 갱신 · 정보이득 기반 단서 추천 · 원본 보존</sub>

## 기술과 실습

| 영역 | 활용 기술 | 프로젝트에서 한 일 |
|---|---|---|
| 모의해킹·진단 | Burp Suite · Nmap · sqlmap · Hydra · WPScan | 웹 공격 재현과 Linux·Windows·Apache 취약점 진단 |
| 리버싱·익스플로잇 | IDA · x32dbg · GDB · pwndbg · pwntools · PEview · UPX | PE·스택 분석, 바이너리 패치·후킹, 메모리 익스플로잇 실습 |
| 디지털 포렌식 | FTK Imager · HxD · KAPE · EZ Tools · RegRipper · Timeline Explorer | 디스크 구조·아티팩트 분석, 수집·처리 결과 검토 |
| 관제·탐지 | Splunk/SPL · Snort · ModSecurity · Sigma · Wireshark | 로그·패킷 분석, 탐지 룰·경보, 대응 후 검증 |
| 인프라·클라우드 | Linux · Windows Server · VMware ESXi · pfSense · VyOS · AWS · OpenTofu | 망 분리·라우팅·방화벽·서버 구성, 클라우드 보안 실습과 IaC 설계 |
| 개발·데이터 | Python · C · C++ · SQL · TypeScript · FastAPI · React · SQLite · Neo4j · Elasticsearch | 프로젝트 개발, 포렌식 파서·학습 코드, 검색·시각화 |

## Practice

### Memory exploitation

전공 과제에서 GDB·pwndbg로 스택과 레지스터를 확인하고 pwntools로 버퍼 오버플로우·ROP·Stack Pivot·포맷 스트링·Canary 우회를 실습했습니다. [VLC 버퍼 오버플로우 분석 기록](https://github.com/acvbbnm/sesac-study-notes/blob/main/악성코드-리버싱/VLC_CVE-2008-4654_버퍼오버플로우_익스플로잇.md)도 정리했습니다.

### Reverse engineering

Crackme 검증 루틴, PE 헤더 복구, 안티디버깅, 코드 케이브·후킹, 악성코드 샘플을 분석했습니다. [분석 기록](https://github.com/acvbbnm/sesac-study-notes/tree/main/악성코드-리버싱)

### Digital forensics

디스크 이미징·해시 검증, MBR/GPT·NTFS/FAT32 구조와 부트 섹터 분석을 실습하고 C로 타임스탬프·파일 시그니처 분석 코드를 작성했습니다. KAPE 처리 결과와 Windows 아티팩트 분석은 [Evidence Atlas](https://github.com/acvbbnm/dfir)로 연결했습니다.

### Cloud and API security

AWS Lambda·API Gateway로 위험도 API를 구성하고 Postman으로 호출 결과를 검증했습니다. boto3로 S3 공개 설정 등 클라우드 보안 구성을 점검했습니다. [S3 설정 진단 기록](https://github.com/acvbbnm/sesac-study-notes/blob/main/클라우드보안/lab3/Lab3_보고서_S3_PublicAccessBlock.md)

## Education

**세종대학교 · 정보보호학과**  
2027년 2월 졸업 예정

시스템해킹과보안 · 디지털포렌식 · 운영체제및보안 · 데이터베이스보안 · 컴퓨터네트워크

**KISIA 청년취업사관학교(SeSAC)**  
AI를 활용한 보안전문가 양성과정 수료

보안관제, 침해사고 대응, 클라우드 보안, 취약점 진단, 리버싱

## Experiments and learning

- [AI 오케스트레이션](https://github.com/acvbbnm/ai_orchestration) · AI CLI 역할 분담 실험과 실패 분석
- [SeSAC 학습 기록](https://github.com/acvbbnm/sesac-study-notes) · 보안 교육 과정 학습·실습 기록

---

[Notion 포트폴리오](https://cooperative-cave-e9b.notion.site/41c70716154e81b289fde409f3bae4c9)
