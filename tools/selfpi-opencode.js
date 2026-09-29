#!/usr/bin/env node
'use strict';

/**
 * OURSELF // SELFPI // OpenCode transport skill
 *
 * SOURCE REALITY
 *   GitHub: situaedmilly/ourself-agent-bridge-kernel
 *   Constitutional agent: .github/agents/ourselftelligence.agent.md
 *   Adapter precedent: adapters/ollama-self.js
 *
 * PURPOSE
 *   Establish a bounded SSH transport from the local /RUORA runtime to the
 *   authenticated SELFPI Ollama service, verify the remote identity, verify
 *   the tunneled Ollama endpoint, and optionally boot OpenCode against it.
 *
 * CONSTITUTIONAL BOUNDARY
 *   transport != identity != authority != actuation
 *   MODEL != AUTHORITY
 *   TOOL ACCESS != ADMISSION
 *   AGENT != GOVERNOR
 *
 * SAFETY
 *   - No remote mutation/install commands.
 *   - No OURSELFD startup.
 *   - No Git mutation.
 *   - SSH is transport only.
 *   - OpenCode receives the Ollama endpoint as cognition substrate only.
 *
 * IMPORTANT
 *   This artifact deliberately owns the SSH forward with -L and
 *   ClearAllForwardings=yes. It does NOT rely on ~/.ssh/config LocalForward,
 *   preventing a duplicate-forward collision with a pre-existing Mac Ollama.
 *
 * DEFAULT TOPOLOGY
 *
 *   /RUORA (Mac)
 *       |
 *       | SSH control master + local forward
 *       v
 *   127.0.0.1:11435
 *       |
 *       | SSH
 *       v
 *   SELFPI / 127.0.0.1:11434
 *       |
 *       v
 *   Ollama
 *
 * USAGE FROM /RUORA
 *   node ./tools/selfpi-opencode.js check
 *   node ./tools/selfpi-opencode.js tunnel
 *   node ./tools/selfpi-opencode.js ollama
 *   node ./tools/selfpi-opencode.js status
 *   node ./tools/selfpi-opencode.js boot
 *   node ./tools/selfpi-opencode.js stop
 *
 * OPTIONAL ENVIRONMENT
 *   SELFPI_ID=SELFPI-001
 *   SELFPI_SSH_ALIAS=selfpi-opencode
 *   SELFPI_REMOTE_HOST=192.168.12.112
 *   SELFPI_REMOTE_OLLAMA_PORT=11434
 *   SELFPI_OLLAMA_LOCAL_PORT=11435
 *   SELFPI_SSH_SOCKET=~/.ssh/selfpi-opencode.sock
 *   SELFPI_OLLAMA_MODEL=ourself-qwen25-7b-kernel:latest
 */

const { spawnSync } = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const CONFIG = Object.freeze({
  selfpiId: process.env.SELFPI_ID || 'SELFPI-001',
  sshAlias: process.env.SELFPI_SSH_ALIAS || 'selfpi-opencode',
  remoteHost: process.env.SELFPI_REMOTE_HOST || '192.168.12.112',
  remoteOllamaPort: Number(process.env.SELFPI_REMOTE_OLLAMA_PORT || 11434),
  localOllamaPort: Number(process.env.SELFPI_OLLAMA_LOCAL_PORT || 11435),
  ollamaModel: process.env.SELFPI_OLLAMA_MODEL || 'ourself-qwen25-7b-kernel:latest',
  socket: process.env.SELFPI_SSH_SOCKET || path.join(os.homedir(), '.ssh', 'selfpi-opencode.sock'),
});

const OLLAMA_URL = `http://127.0.0.1:${CONFIG.localOllamaPort}`;

function die(message, code = 1) {
  console.error(`[SELFPI][ERROR] ${message}`);
  process.exit(code);
}

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    stdio: options.stdio || 'inherit',
    encoding: 'utf8',
    shell: false,
    env: { ...process.env, ...(options.env || {}) },
  });

  if (result.error && !options.allowFailure) {
    die(`${command}: ${result.error.message}`);
  }

  if (!options.allowFailure && result.status !== 0) {
    die(`${command} exited with status ${result.status}`);
  }

  return result;
}

function sshConfigPath() {
  return path.join(os.homedir(), '.ssh', 'config');
}

function assertSshAlias() {
  const file = sshConfigPath();
  if (!fs.existsSync(file)) {
    die(`SSH config not found: ${file}`);
  }

  const text = fs.readFileSync(file, 'utf8');
  const escaped = CONFIG.sshAlias.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const hostPattern = new RegExp(`(^|\\n)\\s*Host\\s+${escaped}(\\s|$)`);

  if (!hostPattern.test(text)) {
    die(`SSH alias '${CONFIG.sshAlias}' is not declared in ${file}`);
  }
}

function controlSocketAlive() {
  const result = run('ssh', ['-S', CONFIG.socket, '-O', 'check', CONFIG.sshAlias], {
    stdio: 'pipe',
    allowFailure: true,
  });
  return result.status === 0;
}

function startTunnel() {
  assertSshAlias();

  if (controlSocketAlive()) {
    console.log('[SELFPI] existing SSH control master is alive');
    verifyOllama();
    return;
  }

  fs.mkdirSync(path.dirname(CONFIG.socket), { recursive: true, mode: 0o700 });

  console.log(`[SELFPI] transport alias=${CONFIG.sshAlias}`);
  console.log(`[SELFPI] remote=${CONFIG.remoteHost}:${CONFIG.remoteOllamaPort}`);
  console.log(`[SELFPI] local Ollama=${OLLAMA_URL}`);

  const result = run('ssh', [
    '-M',
    '-S', CONFIG.socket,
    '-o', 'BatchMode=yes',
    '-o', 'ExitOnForwardFailure=yes',
    '-o', 'ClearAllForwardings=yes',
    '-L', `${CONFIG.localOllamaPort}:127.0.0.1:${CONFIG.remoteOllamaPort}`,
    '-fN',
    CONFIG.sshAlias,
  ], { stdio: 'pipe', allowFailure: true });

  if (result.status !== 0) {
    const stderr = String(result.stderr || '').trim();
    die(`SSH transport failed${stderr ? `: ${stderr}` : ''}`);
  }

  if (!controlSocketAlive()) {
    die('SSH control master did not become reachable');
  }

  console.log('[SELFPI] SSH transport established');
}

function stopTunnel() {
  if (!controlSocketAlive()) {
    console.log('[SELFPI] no active control master');
    return;
  }

  run('ssh', ['-S', CONFIG.socket, '-O', 'exit', CONFIG.sshAlias]);
  console.log('[SELFPI] SSH transport closed');
}

function verifyRemoteIdentity() {
  assertSshAlias();

  const command = [
    'set -eu',
    "printf 'hostname='; hostname",
    "printf 'user='; whoami",
    "printf 'arch='; uname -m",
    "printf 'kernel='; uname -r",
    "printf 'ollama_service='; systemctl is-active ollama 2>/dev/null || true",
  ].join('; ');

  const result = run('ssh', [
    '-o', 'BatchMode=yes',
    '-o', 'ConnectTimeout=5',
    CONFIG.sshAlias,
    command,
  ], { stdio: 'pipe', allowFailure: true });

  process.stdout.write(result.stdout || '');
  process.stderr.write(result.stderr || '');

  if (result.status !== 0) {
    die(`remote identity check failed with status ${result.status}`);
  }
}

function verifyOllama() {
  const result = run('curl', [
    '--fail',
    '--silent',
    '--show-error',
    '--connect-timeout', '3',
    '--max-time', '5',
    `${OLLAMA_URL}/api/tags`,
  ], { stdio: 'pipe', allowFailure: true });

  if (result.status !== 0) {
    die(`tunneled Ollama endpoint unavailable: ${OLLAMA_URL}`);
  }

  let payload;
  try {
    payload = JSON.parse(result.stdout);
  } catch {
    die('Ollama returned non-JSON output');
  }

  const models = Array.isArray(payload.models) ? payload.models : [];
  console.log(`[SELFPI] Ollama reachable: ${OLLAMA_URL}`);
  console.log(`[SELFPI] models visible: ${models.length}`);

  for (const model of models) {
    console.log(`  - ${model.name || '<unnamed>'}  ${model.digest || ''}`.trim());
  }

  const selected = models.find((model) => model.name === CONFIG.ollamaModel);
  console.log(`[SELFPI] selected_model=${CONFIG.ollamaModel}`);
  console.log(`[SELFPI] selected_model_present=${selected ? 'YES' : 'NO'}`);

  return payload;
}

function status() {
  console.log('=== OURSELF // SELFPI // OPENCODE STATUS ===');
  console.log(`SELFPI_ID=${CONFIG.selfpiId}`);
  console.log(`SSH_ALIAS=${CONFIG.sshAlias}`);
  console.log(`SSH_SOCKET=${CONFIG.socket}`);
  console.log(`REMOTE_HOST=${CONFIG.remoteHost}`);
  console.log(`REMOTE_OLLAMA_PORT=${CONFIG.remoteOllamaPort}`);
  console.log(`LOCAL_OLLAMA_ENDPOINT=${OLLAMA_URL}`);
  console.log(`CONTROL_MASTER=${controlSocketAlive() ? 'PRESENT' : 'ABSENT'}`);

  const curl = run('curl', [
    '--fail', '--silent', '--show-error',
    '--connect-timeout', '2', '--max-time', '3',
    `${OLLAMA_URL}/api/tags`,
  ], { stdio: 'pipe', allowFailure: true });

  console.log(`OLLAMA_REACHABLE=${curl.status === 0 ? 'YES' : 'NO'}`);
  console.log('AUTHORITY=NONE');
  console.log('ADMISSION=NOT_ESTABLISHED');
  console.log('ACTUATION=NOT_EXECUTED');
  console.log('EFFECT=NOT_ESTABLISHED');
}

function bootOpenCode() {
  startTunnel();
  verifyOllama();

  console.log('[SELFPI] booting OpenCode');
  console.log(`[SELFPI] OLLAMA_HOST=${OLLAMA_URL}`);
  console.log('[SELFPI] authority=NONE');
  console.log('[SELFPI] execution=NOT_ADMITTED');

  run('opencode', [], {
    env: {
      OLLAMA_HOST: OLLAMA_URL,
      SELFPI_ID: CONFIG.selfpiId,
      SELFPI_SSH_ALIAS: CONFIG.sshAlias,
      SELFPI_OLLAMA_ENDPOINT: OLLAMA_URL,
    },
  });
}

function printContract() {
  console.log(JSON.stringify({
    artifact: 'selfpi-opencode.js',
    executable: true,
    source_reality: {
      github_repository: 'situaedmilly/ourself-agent-bridge-kernel',
      constitutional_agent: '.github/agents/ourselftelligence.agent.md',
      ollama_adapter: 'adapters/ollama-self.js',
    },
    local_boot_root: path.resolve(process.cwd()),
    expected_location: path.join(path.resolve(process.cwd()), 'tools', 'selfpi-opencode.js'),
    selfpi: CONFIG.selfpiId,
    ssh_alias: CONFIG.sshAlias,
    remote_ollama: `127.0.0.1:${CONFIG.remoteOllamaPort}`,
    local_tunnel: OLLAMA_URL,
    authority: 'NONE',
    actuation: 'NOT_EXECUTED',
  }, null, 2));
}

function main() {
  const action = process.argv[2] || 'status';

  switch (action) {
    case 'check':
      verifyRemoteIdentity();
      break;
    case 'tunnel':
      startTunnel();
      verifyOllama();
      break;
    case 'ollama':
      verifyOllama();
      break;
    case 'status':
      status();
      break;
    case 'boot':
    case 'open':
      bootOpenCode();
      break;
    case 'contract':
      printContract();
      break;
    case 'stop':
      stopTunnel();
      break;
    default:
      console.error('Usage: selfpi-opencode.js {check|tunnel|ollama|status|boot|open|contract|stop}');
      process.exit(2);
  }
}

main();
