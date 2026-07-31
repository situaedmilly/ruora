# ROBINHOOD MCP CAPABILITY AUDIT

Mode: read-only capability discovery, schema inspection, authorization verification.
No order was placed, reviewed, modified, canceled, or exercised. No transfer, settings, or watchlist mutation was invoked. Only schemas were inspected for write-capable tools.

## Connection

- MCP server: `robinhood-trading` (tools namespaced `mcp__robinhood-trading__*`)
- Connection: CONNECTED — tool schemas resolved and every invoked call returned live data
- Authentication: AUTHENTICATED — calls returned real account numbers, positions, order history, and realized P&L for a live Robinhood identity
- Transport: UNKNOWN — not exposed by any tool response or by repo config; this MCP is wired into the harness outside `/Users/millysituated/RUORA`
- Server version: not exposed by any tool
- Client version: not exposed by any tool
- Local timestamp (start): 2026-07-30 05:48:41 EDT
- UTC timestamp (start): 2026-07-30T09:48:41Z
- Report generated: 2026-07-30T09:53:03Z
- Repository / branch: `/Users/millysituated/RUORA` @ `main`
- Session root: `/Users/millysituated/.claude/projects/-Users-millysituated-RUORA/922e30dc-60e0-47be-8ee3-dc97d98cf8e8`
- Other configured MCP servers (non-brokerage, not audited here): Canva, Google Drive, Slack, Supabase, PlanetScale, LSEG, Notion, S&P Global (all `claude_ai_*` connectors)

**Connection verdict: `CONNECTED_AUTHENTICATED`**

## Capability Summary

- Total tools discovered: **52**
- Read-only market tools: 14
- Read-only account tools: 15
- Read-only reference tools: 4
- Write-review tools (order simulation): 2
- Write-execution tools (real money/irrevocable): 3
- Write-mutation tools (account state, non-order): 14
- Unknown/unclassifiable tools: 0

Every tool's purpose was determinable from its schema and description — none required invocation to classify.

## Accounts Discovered (sanitized)

`get_accounts` returned 5 brokerage accounts under one identity:

| Account (masked) | Type | Brokerage type | agentic_allowed | option_level |
|---|---|---|---|---|
| ••••4454 (default) | margin | individual | **false** | option_level_3 |
| ••••3742 | cash | ira_roth | false | (empty) |
| ••••6562 | cash | ira_traditional | false | option_level_2 |
| ••••6408 (nickname "Agentic") | cash | individual | **true** | (empty) |
| ••••1511 | margin | joint_tenancy_with_ros | false | (empty) |

**Critical finding:** only one account is agentic-write-eligible, and that account has no options approval. Any write tool requiring `agentic_allowed=true` can act on exactly one account (••••6408), and any options-write tool is additionally blocked there by empty `option_level`. The account with full options access (••••4454, option_level_3) is not agentic-allowed at all.

## Authorization Surface

| Surface | Status |
|---|---|
| Market data | AUTHORIZED |
| Account profile | AUTHORIZED |
| Balances | AUTHORIZED |
| Positions | AUTHORIZED |
| Transactions | AUTHORIZED |
| Equity orders (write) | EXPOSED_NOT_TESTED — gated to 1 of 5 accounts |
| Option orders (write) | EXPOSED_NOT_TESTED — gated to 1 of 5 accounts, and that account lacks any option_level, so effectively UNAUTHORIZED everywhere reachable |
| Scanners (read) | AUTHORIZED |
| Scanners (write: create/update) | EXPOSED_NOT_TESTED |
| Options chains | AUTHORIZED |
| Options quotes | AUTHORIZED |
| Technical indicators | AUTHORIZED |
| Transfers | **UNAVAILABLE** — no such tool exists in this MCP |
| Settings mutation | **UNAVAILABLE** — no such tool exists in this MCP |
| Recurring investments | **UNAVAILABLE** — no create/manage tool exists (order schema has a `placed_agent: recurring/drip` filter value, implying the concept exists in Robinhood's backend, but the MCP exposes no way to originate one) |

Read access is **not** gated by `agentic_allowed` — every read-only account tool succeeded against account ••••4454 despite `agentic_allowed=false` on it. Only the write tools declare an `agentic_allowed=true` requirement in their own schemas/descriptions. Authorization is therefore two-tier: reads are identity-scoped only; writes are additionally allowlisted per-account.

## Verified Market Data (SPY / SPX)

| Field | Tool | Present | Notes |
|---|---|---|---|
| Last / bid / ask | get_equity_quotes | Yes | last=729.54, bid=732.83, ask=732.90 (post-close, extended session) |
| Prior official close | get_equity_quotes | Yes | 729.46 (2026-07-29), separate from live quote |
| Open/high/low/volume | get_equity_fundamentals | Yes | today's session OHLCV + 52-week range, PE, PB, dividend schedule |
| OHLCV bars (daily) | get_equity_historicals | Yes | 21 daily bars returned for a 30-day window |
| L2 order book | get_equity_price_book | Yes | full bid/ask ladder with resting size, 60+ levels each side |
| RSI (14) | get_equity_technical_indicators | Yes | full daily series, no gaps |
| MACD/Bollinger/EMA/SMA/ATR/VWAP/OBV/etc. | get_equity_technical_indicators | Not directly tested, but same tool — schema confirms all listed types accepted | type param covers 17 indicators total |
| Index level (SPX) | get_index_quotes | Yes | 7316.15, live | requires a 2-call chain: get_indexes → id → get_index_quotes |
| Company financials | get_financials | null | SPY is an ETF — no reported financials exist; expected gap, not a failure |
| Earnings | get_earnings_results | empty | SPY is an ETF — no earnings; expected gap, not a failure |
| Market hours / session clock | — | **No dedicated tool** | `get_equity_tradability`'s guide references a `trading://market-hours` resource, not a callable tool; no `get_market_hours` tool exists in the inventory |

## Verified Options Data (SPY, 2026-08-21 expiry, $730 strike)

| Field | Present | Value (call / put) |
|---|---|---|
| Option symbol/instrument id | Yes | UUID per contract |
| Underlying, expiration, strike, type | Yes | SPY / 2026-08-21 / 730.00 / call+put |
| Bid / ask | Yes | 12.62/12.73 (call), 12.46/12.58 (put) |
| Mark / adjusted mark | Yes | 12.675 / 12.68 (call) |
| Last / prior close | Yes | prior close via paired `close` object (20.27 / 7.14) |
| Volume / open interest | Yes | 1,470 / 20,454 (call), 24,384 / 63,811 (put) |
| Implied volatility | Yes | 16.7% (call), 18.1% (put) |
| Delta, gamma, theta, vega, rho | Yes | all 5 greeks present on both legs |
| Contract multiplier | Yes | via chain's `trade_value_multiplier` (100) |
| Tradability / state | Yes | tradable / active |
| Quote timestamp | Yes | `updated_at` on quote |
| Chain identifier | Yes | on `get_option_chains` response |

**Options capability verdict: `FULL_OPTIONS_OBSERVATION`** — chains, instruments, quotes, greeks, IV, OI, and volume all confirmed live and populated.

## Scanner Audit

- `get_scans`: returned 2 user-saved scans ("Untitled Scan" with Aroon+IV filters, "Daily gainers" preset), neither Cortex-managed.
- `get_scanner_filter_specs`: returned 46 valid filter types across FUNDAMENTAL, OPTION, PRICE_VOLUME, TECHNICAL groups, each with supported predicates/intervals/lengths.
- `run_scan("Daily gainers")`: executed successfully, live, 398 matching instruments (equities + crypto mixed), each row carrying the scan's configured columns. Response exceeded the harness's per-call token cap (69.8K chars) and was read back from the on-disk spill file via `jq` rather than dumped in full.
- Scans are account-owned but their *execution* (`run_scan`) does not mutate anything — confirmed read-only.
- Creating/modifying a scan (`create_scan`, `update_scan_filters`, `update_scan_config`) is a real mutation — schema-inspected only, not invoked.

**Scanner verdict: `SCANNER_READ_ONLY`** (for observation purposes — write variants exist but were not exercised)

## Verified Account Read Access

- Account summary (`get_accounts`): 5 accounts, full metadata, sanitized above.
- Balances (`get_portfolio`): tested on 2 accounts — ••••4454 (total_value ≈ $375, cash $200.60, small SPY + crypto holding) and ••••6408 (all-zero, unfunded).
- Equity positions (`get_equity_positions`): 1 open position (SPY, 0.237842 fractional shares, avg cost 739.99) on ••••4454.
- Option positions (`get_option_positions`): 0 open on ••••4454 (empty array, valid result).
- Transactions (`get_pnl_trade_history`): 10 realized closing trades in the last week on ••••4454 — all options (per-contract dollar prices in the $11–$236 range), symbol-only, no counterparty/PII beyond what the account owner already has.
- Order history (`get_equity_orders`, `get_option_orders`): both succeeded and returned exactly 200 orders each (page cap), spanning back to 2021 (equity) and 2022 (options) — cursor-paginated, `placed_agent` values seen: `user`, `expiring_option`. **No `agentic`-placed orders exist in this history**, consistent with the account-gating finding above.
- Tax lots (`get_equity_tax_lots`): 1 open lot on the SPY position, cost basis and short-term status returned correctly.

## Write Surface (schema-inspected only — nothing invoked)

19 tools total:

**WRITE_EXECUTION (real money / irrevocable):** `place_equity_order`, `place_option_order`, `exercise_option`
**WRITE_REVIEW (simulation, explicitly out-of-scope per audit brief):** `review_equity_order`, `review_option_order`
**WRITE_MUTATION (account state, non-order):** `cancel_equity_order`, `cancel_option_order`, `cancel_option_exercise`, `create_watchlist`, `update_watchlist`, `add_to_watchlist`, `remove_from_watchlist`, `follow_watchlist`, `unfollow_watchlist`, `add_option_to_watchlist`, `remove_option_from_watchlist`, `create_scan`, `update_scan_filters`, `update_scan_config`

- **WRITE_SURFACE_EXPOSED: YES**
- **WRITE_SURFACE_REACHABLE_FROM_RBHCB: UNKNOWN** — a repo-wide search of `/Users/millysituated/RUORA` (projects/, systems/, tools/, scripts/, governance/, runtime/) found **no SELFQUANT or RBHCB runtime code**. The only related artifact is a defensive guard in `systems/ourself-agent-bridge/commands/codex.sh:32` — `case "$ROOT" in *selfquant*) BLOCK="SELFQUANT_contamination" ;; esac` — which *blocks* execution if the working root contains "selfquant", i.e. evidence of an isolation boundary, not evidence of a wired integration. Actual reachability can only be verified by auditing the SELFQUANT/RBHCB codebase directly, which does not live in this repository.
- **EXECUTION_AUTHORITY_DEFAULT: FALSE** for 4 of 5 accounts. The one exception (••••6408) is a purpose-built low-privilege account that is additionally unable to trade options (no `option_level`) — so even where execution authority is TRUE, it's capped to equities on a near-empty account.
- **KILL_SWITCH_PRESENT: NO** — no dedicated disable/kill-switch tool exists. The closest control is the per-account `agentic_allowed` flag returned by `get_accounts`, which its own guide describes as "caller-relative" (an allowlist per calling agent identity), not a global switch, and there is no tool in this MCP to flip it.
- **QUARANTINE_VERDICT: PASS** — every write-capable tool was schema-read only; zero invocations.

## Rate Limits and Failure Behavior

- No explicit rate-limit or retry-after metadata was returned by any call (no `429`s encountered from a modest ~25-call sequence).
- **Doc/schema mismatch found:** `get_realized_pnl` failed with `InvalidArgument: un-specified asset class` when `asset_classes` was omitted, even though its own schema documents that parameter as optional ("Omit for all asset classes available on the account"). Retrying with `asset_classes: ["equity"]` succeeded. This is a genuine gap between documented and actual behavior.
- **Size-cap behavior, not a Robinhood rate limit:** `get_equity_orders`, `get_option_orders`, and `run_scan` all returned valid, complete responses that exceeded the harness's per-tool-call token ceiling (155K, 230K, and 70K characters respectively, driven by a 200-order page size and a 398-row scan result). The harness spilled these to disk automatically; they had to be inspected via `jq` rather than read inline. An agent without file-spill support would hard-fail on any account with substantial order history, or any scan matching a broad universe, unless it pre-narrows with `state`/`symbol`/`created_at_gte` filters (equity/option orders) — there is no documented way to shrink a `run_scan` result short of narrowing the scan's own filters.
- `get_indexes` alone returns an effectively empty snapshot (`current_value`, `name`, `updated_at` all blank) — a live index value requires a second call, `get_index_quotes`, chained off the `id` from `get_indexes`.
- No stale-session or auth-expiry behavior was observed — every call in this session succeeded or failed with a clean, sanitized error (no secrets or tokens leaked in error text).

## Failures and Gaps

- **Unauthorized:** none observed — no read call was rejected for lack of permission.
- **Unavailable:** transfers/ACH, account-settings mutation, recurring-investment creation, and a dedicated `get_market_hours` tool — none exist in this MCP.
- **Broken:** `get_realized_pnl` requires `asset_classes` in practice despite documenting it as optional (see above).
- **Schema unknown:** none — all 52 tools fully typed via their JSONSchema.
- **Stale or incomplete:** `get_indexes` snapshot fields are structurally empty; must pair with `get_index_quotes`.
- **Not exercised (by design, per audit boundary):** `get_earnings_calendar`, `get_watchlist_items`, `get_option_historicals` — schemas confirmed, live call skipped as redundant with sibling tools already proven live.

## Final Capability Matrix

| Tool | Exists | Authorized | Called | Usable | Mutating | Notes |
|---|---|---|---|---|---|---|
| get_accounts | Y | Y | Y | Y | N | 5 accounts returned |
| get_portfolio | Y | Y | Y | Y | N | tested on 2 accounts |
| get_equity_positions | Y | Y | Y | Y | N | |
| get_option_positions | Y | Y | Y | Y | N | empty, valid |
| get_equity_orders | Y | Y | Y | Y | N | hit 200-order page cap / token spill |
| get_option_orders | Y | Y | Y | Y | N | hit 200-order page cap / token spill |
| get_equity_tax_lots | Y | Y | Y | Y | N | |
| get_pnl_trade_history | Y | Y | Y | Y | N | |
| get_realized_pnl | Y | Y | Y (2nd try) | Y | N | fails without explicit asset_classes — doc bug |
| get_equity_tradability | Y | Y | Y | Y | N | |
| get_option_level_upgrade_info | Y | Y | Y | Y | N | |
| get_watchlists | Y | Y | Y | Y | N | 16 lists, incl. custom names |
| get_watchlist_items | Y | Y | N | presumed Y | N | schema-only |
| get_option_watchlist | Y | Y | Y | Y | N | empty |
| get_popular_watchlists | Y | Y | Y | Y | N | |
| get_scans | Y | Y | Y | Y | N | 2 scans |
| get_scanner_filter_specs | Y | Y | Y | Y | N | 46 filters |
| run_scan | Y | Y | Y | Y | N | 398 rows, token spill |
| get_equity_quotes | Y | Y | Y | Y | N | |
| get_equity_historicals | Y | Y | Y | Y | N | |
| get_equity_technical_indicators | Y | Y | Y | Y | N | RSI tested; 16 other types schema-confirmed |
| get_equity_price_book | Y | Y | Y | Y | N | |
| get_equity_fundamentals | Y | Y | Y | Y | N | |
| get_financials | Y | Y | Y | Y (null result) | N | SPY has none — expected |
| get_earnings_calendar | Y | Y | N | presumed Y | N | schema-only |
| get_earnings_results | Y | Y | Y | Y (empty result) | N | SPY has none — expected |
| get_index_quotes | Y | Y | Y | Y | N | needs id from get_indexes |
| get_indexes | Y | Y | Y | Y (partial) | N | snapshot fields empty |
| get_option_chains | Y | Y | Y | Y | N | 36 SPY expirations |
| get_option_historicals | Y | Y | N | presumed Y | N | schema-only |
| get_option_instruments | Y | Y | Y | Y | N | |
| get_option_quotes | Y | Y | Y | Y | N | full greeks confirmed |
| search | Y | Y | Y | Y | N | |
| add_to_watchlist | Y | Y (acct-gated) | N | untested | Y | schema-only |
| remove_from_watchlist | Y | Y (acct-gated) | N | untested | Y | schema-only |
| create_watchlist | Y | Y (acct-gated) | N | untested | Y | schema-only |
| update_watchlist | Y | Y (acct-gated) | N | untested | Y | schema-only |
| follow_watchlist | Y | Y (acct-gated) | N | untested | Y | schema-only |
| unfollow_watchlist | Y | Y (acct-gated) | N | untested | Y | schema-only |
| add_option_to_watchlist | Y | Y (acct-gated) | N | untested | Y | schema-only |
| remove_option_from_watchlist | Y | Y (acct-gated) | N | untested | Y | schema-only |
| create_scan | Y | Y (acct-gated) | N | untested | Y | schema-only |
| update_scan_filters | Y | Y (acct-gated) | N | untested | Y | schema-only |
| update_scan_config | Y | Y (acct-gated) | N | untested | Y | schema-only |
| review_equity_order | Y | agentic_allowed-gated | N (forbidden by brief) | untested | N (simulation) | schema-only |
| review_option_order | Y | agentic_allowed-gated | N (forbidden by brief) | untested | N (simulation) | schema-only |
| place_equity_order | Y | agentic_allowed-gated | N (forbidden) | untested | Y (real money) | schema-only |
| place_option_order | Y | agentic_allowed + option_level-gated | N (forbidden) | untested | Y (real money) | schema-only |
| cancel_equity_order | Y | agentic_allowed-gated | N (forbidden) | untested | Y | schema-only |
| cancel_option_order | Y | agentic_allowed-gated | N (forbidden) | untested | Y | schema-only |
| cancel_option_exercise | Y | agentic_allowed-gated | N (forbidden) | untested | Y | schema-only |
| exercise_option | Y | agentic_allowed + option_level-gated | N (forbidden) | untested | Y (irrevocable) | schema-only |

## Final Verdict

**`ROBINHOOD_MCP_FULL_READ_ONLY_OBSERVATION_READY`**

Market data (equities, indexes, technicals, L2 book), full options observation (chains, instruments, quotes, greeks, IV, OI), scanner read+execute, and account read (accounts, portfolio, positions, orders, tax lots, realized P&L) are all live, authenticated, and confirmed working end-to-end on SPY/SPX. The write surface exists (19 tools) but is real, exposed, and structurally narrow: only one of five accounts is agentic-write-eligible, and that account cannot trade options at all. No SELFQUANT/RBHCB execution runtime was found anywhere in this repository to assess further reachability — that check has to happen in whatever repo actually hosts that runtime.

## Final Witness

1. **MCP server discovered:** `robinhood-trading`
2. **Exact tool count:** 52
3. **Complete classified inventory:** see Final Capability Matrix above (14 market / 15 account / 4 reference / 2 review / 3 execution / 14 mutation)
4. **Safe calls executed:** 30 live calls, all succeeded (1 required a parameter correction — see `get_realized_pnl`)
5. **Safe calls that failed:** `get_realized_pnl` on first attempt (doc/schema mismatch, self-corrected)
6. **Options schema verdict:** `FULL_OPTIONS_OBSERVATION`
7. **Scanner verdict:** `SCANNER_READ_ONLY` (write variants exist, untested)
8. **Account-read verdict:** fully verified — accounts, portfolio, positions, orders, tax lots, realized/trade P&L all live
9. **Write-surface quarantine verdict:** `PASS` — zero write invocations; reachability from any external trading runtime is `UNKNOWN` because no such runtime exists in this repo
10. **Report paths:** `reports/robinhood_mcp_audit_20260730T095303Z.md`, `reports/robinhood_mcp_audit_latest.md`
11. **Remaining unknowns:** MCP transport/version; whether a SELFQUANT/RBHCB runtime exists elsewhere on this machine and, if so, whether it imports any write tool; whether `agentic_allowed` can be toggled by the account holder inside the Robinhood app itself
12. **Smallest next lawful audit action:** locate the actual SELFQUANT/RBHCB codebase (outside `/Users/millysituated/RUORA`) and grep it for `place_equity_order`, `place_option_order`, `exercise_option`, or any `mcp__robinhood-trading__` write-tool import — that is the only way to close the `WRITE_SURFACE_REACHABLE_FROM_RBHCB` unknown.
