<h1 align="center">김병우 · Security Engineering</h1>

<p align="center"><b>로그에서 공격의 흐름을 읽고, 조사 과정을 도구로 만듭니다.</b></p>

<p align="center">SOC & Detection Engineering · Digital Forensics · Cloud Incident Response</p>

<p align="center">
  <a href="https://cooperative-cave-e9b.notion.site/41c70716154e81b289fde409f3bae4c9"><img alt="Notion Portfolio" src="https://img.shields.io/badge/Notion-Portfolio-172554?style=flat-square&logo=notion&logoColor=white"></a>
  <a href="https://github.com/acvbbnm?tab=repositories"><img alt="Project Repositories" src="https://img.shields.io/badge/GitHub-Projects-0F766E?style=flat-square&logo=github&logoColor=white"></a>
</p>

---

## About

세종대학교 정보보호학과에서 보안을 공부하며, **공격 재현 → 탐지·분석 → 증거 검토**를 직접 연결하는 프로젝트를 진행했습니다.

클라우드 사고 대응의 어려움을 실무자 설문으로 살펴보고 사고조사 가이드로 연결했습니다. 이후 가상 기업망을 구축해 공격과 탐지 결과를 대조하고, 원본 근거까지 되짚을 수 있는 포렌식 분석 도구를 개발했습니다.

- **관측과 판단** — 경보 발생과 공격 성공을 구분합니다.
- **근거와 원본** — 분석 결과를 로그·출처·해시로 연결합니다.
- **구현과 검증** — 코드, 로컬 검증, 실제 배포의 범위를 나누어 기록합니다.

## Selected projects

### ☁️ [AI Sherpa](https://github.com/acvbbnm/cloud)

**다음에 볼 로그를 안내하는 클라우드 사고조사 가이드** · 정보보호 캡스톤 / 4인 팀 팀장

실무자 설문에서 확인한 조사 병목을 도구의 요구사항으로 연결했습니다. 사고 추적 엔진·수집 가이드·로그 정규화·프론트엔드 연동을 맡고 프로젝트를 총괄했습니다.

`조사 설계` `베이즈 갱신` `정보이득 기반 단서 추천` `원본 보존`

### 🛡️ [SIEM 공격 탐지·대응 실습](https://github.com/acvbbnm/siem-project)

**공격 경로와 탐지의 사각지대를 대조한 가상 SOC** · 개인 프로젝트

공격망·DMZ·내부망·관리망을 분리하고 Snort·WAF·서버 로그를 Splunk에서 분석했습니다. 커스텀 룰 9개, 상관분석 쿼리 7종, Alert 5종과 사건 일지 6건을 정리했습니다.

`Splunk` `Snort` `ModSecurity` `탐지·미탐 분석` `차단 후 재검증`

→ [최종 보고서](https://github.com/acvbbnm/siem-project/blob/main/phase4-soc/final-report.md)

### 🔎 [Evidence Atlas](https://github.com/acvbbnm/dfir)

**포렌식 판단을 원본 근거로 되짚는 시간축·관계 그래프 도구** · 개인 프로젝트

KAPE CSV 산출물의 원래 행·해시·시각 의미를 보존하고, 시간축과 공유 참조 그래프로 탐색하도록 만들었습니다. Sigma 탐지 후보·로컬 AI 가설과 manifest 기반 사건 가져오기를 연결했습니다.

`Python` `SQLite` `Neo4j` `Elasticsearch` `Sigma` `근거 보존`

→ [설계서](https://github.com/acvbbnm/dfir/blob/main/DESIGN.md) · AWS 확장은 **코드·로컬 검증 단계 / 실제 AWS 미배포**

## Skills & practice

| 영역 | 활용 기술 | 프로젝트에서 한 일 |
|---|---|---|
| 보안관제·탐지 | Splunk · Snort · ModSecurity | 수집·상관분석, 경보 판정, 탐지 사각지대 분석과 대응 검증 |
| 포렌식·증거 | KAPE · Sigma · SQLite · Neo4j | 아티팩트 적재, 원본·해시·시각 의미 보존, 관계 탐색 |
| 검색·개발 | Python · FastAPI · React/TypeScript · Elasticsearch/Kibana | 사고 추적·수집 가이드, 로그 정규화, 분석 화면과 검색·집계 |
| 클라우드·자동화 | AWS · OpenTofu · Velociraptor | 증거 수집 흐름과 계정 분리 설계, IaC·로컬 검증 |
| AI 활용·분석 | IDA · MCP · Ollama · AI CLI | 분석 도구 연계, 근거 인용 검증, 에이전트 협업 실험 |

## Education

**세종대학교 · 정보보호학과**  
2027년 2월 졸업 예정

시스템해킹과보안 · 디지털포렌식 · 운영체제및보안 · 데이터베이스보안 · 컴퓨터네트워크 등 이수

**KISIA 청년취업사관학교(SeSAC)**  
AI를 활용한 보안전문가 양성과정 수료

보안관제·침해사고 대응·클라우드 보안·취약점 진단·리버싱을 학습하고 프로젝트에 적용했습니다.

## Experiments & learning

- 🤖 [AI 오케스트레이션](https://github.com/acvbbnm/ai_orchestration) — 여러 AI CLI의 역할 분담을 실험하고 실행 기록에서 실패 원인과 개선 구조를 분석했습니다.
- 📚 [SeSAC 학습 기록](https://github.com/acvbbnm/sesac-study-notes) — 보안관제·침해사고 대응·클라우드 보안·리버싱 등의 학습과 실습을 모았습니다.

---

[Notion에서 프로젝트 문서와 실습 증적 보기 →](https://cooperative-cave-e9b.notion.site/41c70716154e81b289fde409f3bae4c9)
