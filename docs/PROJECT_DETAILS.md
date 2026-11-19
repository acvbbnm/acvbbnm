# 김병우

Security Engineering · Digital Forensics · Reverse Engineering

<p align="center"><a href="https://cooperative-cave-e9b.notion.site/41c70716154e81b289fde409f3bae4c9">Notion 포트폴리오</a> · <a href="https://github.com/acvbbnm?tab=repositories">GitHub 프로젝트</a></p>

---

## About

세종대학교 정보보호학과에서 보안을 공부하며, 공격을 재현하고, 탐지·분석하고, 증거를 검토하는 과정을 한 프로젝트 안에서 직접 이어 보았습니다.

클라우드 사고 대응의 어려움을 실무자 설문으로 살펴보고 사고조사 가이드로 연결했습니다. 이후 가상 기업망을 구축해 공격과 탐지 결과를 대조하고, 원본 근거까지 되짚을 수 있는 포렌식 분석 도구를 개발했습니다.

## Selected projects

### [AI Sherpa](https://github.com/acvbbnm/cloud)

다음에 볼 로그를 안내하는 클라우드 사고조사 가이드. 정보보호 캡스톤, 4인 팀 팀장.

실무자 설문에서 확인한 조사 병목을 도구의 요구사항으로 연결했습니다. 사고 추적 엔진·수집 가이드·로그 정규화·프론트엔드 연동을 맡고 프로젝트를 총괄했습니다.

핵심 기법: 조사 설계, 베이즈 갱신, 정보이득 기반 단서 추천, 원본 보존

### [SIEM 공격 탐지·대응 실습](https://github.com/acvbbnm/siem-project)

공격 경로와 탐지의 사각지대를 대조한 가상 SOC. 개인 프로젝트.

공격망·DMZ·내부망·관리망을 분리하고 Snort·WAF·서버 로그를 Splunk에서 분석했습니다. 커스텀 룰 9개, 상관분석 쿼리 7종, Alert 5종과 사건 일지 6건을 정리했습니다.

핵심 기법: Splunk, Snort, ModSecurity, 탐지·미탐 분석, 차단 후 재검증

[최종 보고서](https://github.com/acvbbnm/siem-project/blob/main/phase4-soc/final-report.md)

### [Evidence Atlas](https://github.com/acvbbnm/dfir)

포렌식 판단을 원본 근거로 되짚는 시간축·관계 그래프 도구. 개인 프로젝트.

KAPE CSV 산출물의 원래 행·해시·시각 의미를 보존하고, 시간축과 공유 참조 그래프로 탐색하도록 만들었습니다. Sigma 탐지 후보·로컬 AI 가설과 manifest 기반 사건 가져오기를 연결했습니다.

핵심 기법: Python, SQLite, Neo4j, Elasticsearch, Sigma, 근거 보존

[설계서](https://github.com/acvbbnm/dfir/blob/main/DESIGN.md). AWS 확장은 코드와 로컬 검증까지 마쳤고, 실제 AWS에는 아직 배포하지 않았습니다.

## Skills and practice

| 영역 | 활용 기술 | 프로젝트에서 한 일 |
|---|---|---|
| 모의해킹·진단 | Burp Suite · Nmap · sqlmap · Hydra · WPScan | 웹 공격 재현과 Linux·Windows·Apache 취약점 진단 |
| 리버싱·익스플로잇 | IDA · x32dbg · GDB · pwndbg · pwntools · PEview · UPX | PE·스택 분석, 바이너리 패치·후킹, 메모리 익스플로잇 실습 |
| 디지털 포렌식 | FTK Imager · HxD · KAPE · EZ Tools · RegRipper · Timeline Explorer | 디스크 구조·아티팩트 분석, 수집·처리 결과 검토 |
| 관제·탐지 | Splunk/SPL · Snort · ModSecurity · Sigma · Wireshark | 로그·패킷 분석, 탐지 룰·경보, 대응 후 검증 |
| 인프라·클라우드 | Linux · Windows Server · VMware ESXi · pfSense · VyOS · AWS · OpenTofu | 망 분리·라우팅·방화벽·서버 구성, 클라우드 보안 실습과 IaC 설계 |
| 개발·데이터 | Python · C · C++ · SQL · TypeScript · FastAPI · React · SQLite · Neo4j · Elasticsearch | 프로젝트 개발, 포렌식 파서·학습 코드, 검색·시각화 |
| API·분석 도구 | Postman · Talend · IDA/MCP · Ollama · AI CLI | API 테스트 도구 사용, 분석 도구 연계와 자동화 실험 |

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

시스템해킹과보안 · 디지털포렌식 · 운영체제및보안 · 데이터베이스보안 · 컴퓨터네트워크 등 이수

**KISIA 청년취업사관학교(SeSAC)**  
AI를 활용한 보안전문가 양성과정 수료

보안관제·침해사고 대응·클라우드 보안·취약점 진단·리버싱을 학습하고 프로젝트에 적용했습니다.

## Experiments and learning

- [AI 오케스트레이션](https://github.com/acvbbnm/ai_orchestration). 여러 AI CLI의 역할 분담을 실험하고 실행 기록에서 실패 원인과 개선 구조를 분석했습니다.
- [SeSAC 학습 기록](https://github.com/acvbbnm/sesac-study-notes). 보안관제, 침해사고 대응, 클라우드 보안, 리버싱의 학습과 실습을 모았습니다.

---

[Notion에서 프로젝트 문서와 실습 증적 보기](https://cooperative-cave-e9b.notion.site/41c70716154e81b289fde409f3bae4c9)
