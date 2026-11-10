# 现有Skill增量实施清单 · 2026-11-10

执行 [Issue #10](https://github.com/radonpoloniumzzy-boop/Xiaohongshu-technology/issues/10)，承接#8/#9反馈及#4/#6既有审计/冻结。用户明确授权本机实际可写Skill增量编辑；本交付包含真实写入，不以仓库报告代替实施。只公开脱敏记录，不公开私有Skill全文、patch、绝对路径或素材。

## 现场与调用关系

实际定位5个主要入口与4个相关字幕/封面模块，备份86个相关文本/配置/脚本文件；这不是声称读取全机所有Skills。实际使用入口与当前共享索引核对，参考研究入口解析到共享运行目录，其余按真实安装目录读取。修改前无对应独立Skill Git仓库，采用本机原字节备份、前后SHA、逐文件patch与受控回滚交付，不假冒公开PR包含私有源码。

责任分配维持现有结构：总流程研究 → xhs选题证据引用；写手供需判断复用同一引用，幽默与口播审查留在写手；字幕合同集中在生产引用，两条相关入口只做账号路由；封面规则留在原包装发布引用。没有新建替代Skill、数据库或总控。

## 真实修改文件与版本

总流程v2→v2.1，写手v0.3.2→v0.3.3；其他文件以2026-11-10前后SHA为版本身份。下表为SHA-256前12位，完整指纹和可复原差异仅存本机受控交接包。

| 实际文件的逻辑位置 | 修改前 | 修改后 | 脱敏diff摘要 |
|---|---|---|---|
| `SKILLS_ROOT/kiwi-motion-typography/SKILL.md` | c46fc736aac7 | 7be5e54eca62 | 只增账号字幕优先路由，不改变其他项目的通用排版。 |
| `SKILLS_ROOT/tech-short-video-writer/references/humor-mechanisms.md` | 新增 | 356c47912d73 | 新增12条可编辑小表：10个长期机制、2个有来源的历史梗。 |
| `SKILLS_ROOT/tech-short-video-writer/references/information-humor-and-solar-case.md` | 65f3b4103679 | 025876cfa927 | 原创幽默与历史梗引用；真人口播仅文字演绎准备。 |
| `SKILLS_ROOT/tech-short-video-writer/references/self-check.md` | b26219ee274d | 7d7bfb20dc38 | 按事实、技术信息、自然好笑、口播与作者视角顺序审稿。 |
| `SKILLS_ROOT/tech-short-video-writer/references/topic-demand-validation.md` | 7222db7ee9a9 | 76a992aa3934 | 评分不吞掉unknown；研究入围不等于可录可剪。 |
| `SKILLS_ROOT/tech-short-video-writer/SKILL.md` | 183b012ca2a9 | 9a4d3d43a763 | 版本及必读链增量，分开评估信息、专业、趣味和作者视角。 |
| `SKILLS_ROOT/tech-video-shot-planner/SKILL.md` | 8202d6c935c8 | 1ca58734a2fb | 选镜接入同一字幕契约，不复制第二套参数。 |
| `SKILLS_ROOT/tech-video-workflow/references/account-profile.md` | ecc276f5d42c | 74aee1452052 | 去掉近期国内热度的统一资格门；固化本账号单行语义字幕偏好。 |
| `SKILLS_ROOT/tech-video-workflow/references/production.md` | 81509a349f12 | f30107318b33 | 集中维护单行字幕、语义分段、相对主内容定位及手机QA。 |
| `SKILLS_ROOT/tech-video-workflow/references/publish.md` | 6890fdd1e647 | 1360ee746471 | 先审真实封面，真实主体/可编辑文字层、方向比较与四封面保留。 |
| `SKILLS_ROOT/tech-video-workflow/references/research.md` | 8912fbe04150 | f94ba65bf82b | 三路线与研究/制作两道门接续，排重、反例、成本和未知保留。 |
| `SKILLS_ROOT/tech-video-workflow/references/tooling.md` | b4d7088c2548 | fb28038568b5 | 设计排字与AI视觉资产生成分工，沿用现有工具。 |
| `SKILLS_ROOT/tech-video-workflow/SKILL.md` | 6eb17cd151f9 | 8b45ad220e3b | 总入口更新版本、按证据路线研究、字幕和封面分层路由。 |
| `SKILLS_ROOT/xhs-content-validation/references/topic-evidence-routes.md` | 新增 | 858e944a8087 | 新增轻量共享引用：A/B/C、独立性、去重、止损与冻结边界。 |
| `SKILLS_ROOT/xhs-content-validation/SKILL.md` | 6fa760ac6ff0 | 9fe3239d7c1b | 研究先分路线再选工具，不把缺国内数据当需求失败。 |

## 规则增量与不变项

- 选题按前沿探索、多作者跨时间验证、海外迁移分路；市场未知不直接误淘汰，但研究入围不放宽制作硬门。独立作者、来源簇、普通对照、推广与发布龄分别查，不承诺自然爆款。
- 文风把信息性、技术完整、幽默和作者好奇视角分开看；热梗仅辅助原创。12条小表含10个长期机制和2个已核历史用法，当前流行度未证，不搬影音、长台词或模仿声线。先复用既有机制引用；个人知识查询未得到可采纳的专用梗库，未把待审摘要当正式依据。
- 字幕按用户最新补充：每时刻一行，长句拆成连续完整意群，不从词或关键短语中间切开。相对主要动作区下边沿约0.5字高、字号约+10%仅为候选；实际测宽、手机安全区、动作和原文字保护优先，分段改动需真实音频复核，不编落词时间。
- 封面先看真实成品诊断AI感，不预设唯一审美。真实/已授权主体与可编辑标题层优先，AI可辅助背景/创意但不造产品事实；保留1主+3PK，方向样图未确认不批量重制。
- 既有来源核验、事实边界、素材/许可、反例、淘汰、事前冻结、完整关注和用户发布授权继续保留。原片、已录稿、音色、音乐、作品、草稿和账号未被本轮修改。

## 明确未改的模块

`public-media-ingest`继续负责安全采集与来源/许可，不承担市场入围策略，故不强行扩写。`reference-research`已具备原作者、实际查看、数据口径、反例、偏差与研究/复用分离规则；本次特定三路线由运营模块维护，避免两套真源。`remotion-captions`的字幕数据类型和导入能力未改，排版偏好由账号合同接管；`oil-cover`是指定风格子模块，未把它改成所有封面的默认。

## 兼容性与交付范围

5个修改Skill的既有结构校验通过；新增本地引用无缺失。两条账号路由只对本账号口播字幕生效，其他项目的标题卡/标签等通用两行规则保持。除两个轻量引用外不增Skill文件结构，不动渲染器、依赖、采集脚本、账号授权或现有生产参数。实际行为回归与未验项见[验收和回滚](skill-regression-and-reversal-20261110.md)。
