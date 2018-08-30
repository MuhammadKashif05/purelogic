
/**
 * Return 'arg' if it's not undefined, otherwise 'def'.
 */
function defaultArg(arg, def) {
  return typeof arg !== 'undefined' ? arg : def;
}

/**
 * Sensible version of setTimeout.
 */
function newCallback(seconds, callback) {
  setTimeout(callback, seconds * 1000);
}

/**
 * Sensible version of setInterval; calls function immediately (unless the
 * optional 'immediate' is false), then in intervals.
 */
function startInterval(seconds, callback, immediate) {
  if (defaultArg(immediate, true)) {
    callback();
  }
  return setInterval(callback, seconds * 1000);
}

/**
 * Enable or disable everything in the passed jQuery object.
 */
function setEnabled(query, enabled) {
  if (enabled) {
    query.removeAttr('disabled');
  }
  else {
    query.attr('disabled', 'disabled');
  }
}

function jsonPost(url, obj, onComplete) {
  var completeValid = typeof onComplete !== 'undefined';
  $.ajax(url, {
    type: 'POST',
    data: JSON.stringify(obj),
    dataType: 'json',
    processData: false,
    success: function(data, textStatus, jqXHR) {
      if (data == 'true') {
        if (completeValid) {
          onComplete(true);
        }
      }
      else {
        console.log('Server error');
        if (completeValid) {
          onComplete(false);
        }
      }
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.log('Server call failed');
      if (completeValid) {
        onComplete(false);
      }
    }
  });
}

/**
 * Regularly read from URL (every 'interval' seconds), setting the content
 * of 'element' to the HTML returned.
 * 'pauseButton' (optional) will allow updates to be stopped/restarted.
 */
function startContentUpdates(url, element, interval, pauseButton) {
  var intervalId;
  function startUpdates() {
    intervalId = startInterval(interval, function() {
      $.get(url, function(data) {
        element.html(data);
      });
    });
  }
  startUpdates();

  if (typeof pauseButton !== 'undefined') {
    pauseButton.click(function() {
      if (intervalId != 0) {
        clearInterval(intervalId);
        intervalId = 0;
        pauseButton.html('Start Updates');
      }
      else {
        startUpdates();
        pauseButton.html('Pause Updates');
      }
    });
  }
}

/**
 * Write a message to the debug console. The console is created on the first
 * call to this function.
 */
function debugConsole(message) {
  var container = $('#debug-log');
  if (container.length == 0) {
    $('body').append('<div id="debug-log" style="position: absolute; z-index: 100000; padding: 10px; top: 10px; left: 10px; right: 10px; height: 400px; background: rgba(0, 0, 0, 0.5); color: white; font-size: 10px; font-family: sans-serif;"></div>');
    container = $('#debug-log');
  }
  container.append(message + '<br>');
}
