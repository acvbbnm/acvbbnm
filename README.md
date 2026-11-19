<h2 align="center">김병우</h2>

<p align="center">Security Engineering · Digital Forensics · Reverse Engineering</p>

<p align="center">모의해킹·리버싱·포렌식 실습과 보안 분석 도구 개발을 기록합니다.</p>

<p align="center">세종대학교 정보보호학과 · 2027년 2월 졸업 예정</p>

<p align="center"><a href="https://cooperative-cave-e9b.notion.site/41c70716154e81b289fde409f3bae4c9">Notion Portfolio</a> · <a href="docs/PROJECT_DETAILS.md">Projects & Practice</a></p>

## Tech stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/skills/stack-dark.png">
  <img src="assets/skills/stack-light.png" width="720" alt="Digital Forensics: KAPE, FTK Imager, EZ Tools, RegRipper, Timeline Explorer, HxD. Detection and Response: Splunk/SPL, Sigma, Snort, ModSecurity, Wireshark. Reverse Engineering: IDA, x32dbg, GDB, pwndbg, pwntools, PEview, UPX. Offensive Security: Burp Suite, Nmap, sqlmap, Hydra, WPScan. Infrastructure and Cloud: Linux, Windows Server, AWS, VMware ESXi, pfSense, VyOS, OpenTofu. Development and Data: FastAPI, React, SQLite, Elasticsearch, Neo4j, Git, Postman, Talend. Languages: Python, C, C++, TypeScript, SQL, x86/x64 Assembly.">
</picture>

## Projects

### [Evidence Atlas](https://github.com/acvbbnm/dfir)

KAPE 산출물을 시간축과 관계 그래프로 탐색하는 DFIR 분석 도구입니다. 원본 행, SHA-256, 시각의 의미를 그대로 보존합니다. Sigma 탐지 후보와 로컬 AI 분석을 연결했습니다.

사용 기술: Python, SQLite, Neo4j, Elasticsearch, Sigma

### [SIEM Lab](https://github.com/acvbbnm/siem-project)

가상 기업망을 구축하고 모의해킹, 로그 수집, 탐지 룰 작성, 관제 대응을 직접 수행한 개인 실습입니다. 공격 결과와 경보를 대조했고, IP를 차단한 뒤 다시 공격해 차단을 확인했습니다.

사용 기술: VMware ESXi, pfSense, Splunk, Snort, ModSecurity

### [AI Sherpa](https://github.com/acvbbnm/cloud)

클라우드 침해사고에서 다음에 확인할 로그와 수집 방법을 안내하는 조사 가이드입니다. 4인 캡스톤 팀의 팀장으로 사고 추적 엔진, 로그 정규화, 수집 가이드, 화면 연동을 맡았습니다.

사용 기술: Python, FastAPI, React, TypeScript, AWS

## Archive

- [AI 오케스트레이션](https://github.com/acvbbnm/ai_orchestration) · AI CLI에 역할을 나눠 맡기고 실행 기록을 분석한 실험
- [SeSAC 학습 기록](https://github.com/acvbbnm/sesac-study-notes) · 웹 보안, 리버싱, 취약점 진단, 네트워크·클라우드 보안 실습
- [실습 분야 자세히 보기](docs/PROJECT_DETAILS.md#practice) · 메모리 익스플로잇, 디스크·아티팩트 분석, AWS API 실습
