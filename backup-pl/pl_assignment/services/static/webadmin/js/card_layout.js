/**
 * Layout the specified pane in the specified view.
 */
function layoutPane(container, pane, view) {
  var paneQ = container.find('#pane-' + pane.id);
  paneQ.css({width: view.width + 'px', height: view.height + 'px'});
  for (var i = 0; i < pane.layers.length; i ++) {
    var layer = pane.layers[i];
    paneQ.find('#layer-' + layer.id).css({
      left: layer.x - view.x_offset,
      top: layer.y,
      width: layer.w,
      height: layer.h
    });
  }
}

/**
 * Layout all panes in the passed view.
 */
function layoutAllPanes(container, bg, panes, view) {
  if (view.frame) {
    container.find('.device-frame').attr({
      src: view.frame.image,
      width: view.frame.width,
      height: view.frame.height
    });
    container.find('.pane-preview-container').css({
      left: view.frame.inset_x,
      top: view.frame.inset_y,
    });
  }
  container.find('.pane-preview-container').css({
    width: view.width,
    height: view.height
  });
  layoutPane(container, bg, view);
  for (var i = 0; i < panes.length; i ++) {
    layoutPane(container, panes[i], view);
  }
}
